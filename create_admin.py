import glob, re, sys 

## 引数の指定がある場合: 特定のアプリのmodels.pyに対して実行する。
## 引数の指定が無い場合: プロジェクトの全アプリのmodels.pyに対して実行する。

if len(sys.argv) > 1:
    models_paths    = glob.glob(f"./{sys.argv[1]}/models.py")
else:
    models_paths    = glob.glob("./*/models.py")

admin_paths     = [ models_path.replace("models", "admin") for models_path in models_paths ]

# すべてのmodels.pyを順次読み込み
for models_path,admin_path in zip(models_paths, admin_paths):

    #====admin.pyの冒頭===========================
    with open(models_path, "r") as mf:
    
        # models.pyを文字列で読み込み
        models_code     = mf.read()
        model_classes   = re.findall(r'class (\w+)\(models\.Model\):', models_code)

        # admin.pyのimport部を作成
        import_models   = ""
        for model_class in model_classes:
            import_models += f"{model_class},"
        
        import_models   = import_models.rstrip(",")

        # admin.pyのコードを作る。
        admin_code      = [ "# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/== #\n"]
        admin_code.append( f"from django.contrib import admin\nfrom .models import {import_models}\n" )

    #====admin.pyの冒頭===========================

    #====admin.pyの本体===========================

    with open(models_path, "r") as mf:

        # models.pyをリストで読みこみ
        models_codes    = mf.readlines()
        fields_list     = []

        for models_code in models_codes:
            print(models_code)
            
            # モデルクラス名を取得
            model_name  = re.search(r'class (\w+)\(models\.Model\):', models_code)

            if model_name:
            
                # バリデーション対象のフィールドがあれば追加。
                if fields_list:
                    admin_code.append(f"    list_display\t= " + str(["id"]+fields_list) + "\n")
                    fields_list = []
                
                # モデルクラス名を元に、フォームクラスを作る。
                admin_code.append( f"class {model_name.group(1)}Admin(admin.ModelAdmin):")

            # モデルフィールド名を取得
            field_name = re.search(r'(\w+).*=\s*models\.', models_code)
            if field_name:
                # ここでManyToManyは除外
                if "ManyToManyField" not in field_name.group(1):
                    fields_list.append(field_name.group(1))


        # バリデーション対象のフィールドがあれば追加。
        if fields_list:
            admin_code.append(f"    list_display\t= " + str(["id"]+fields_list) + "\n")
            fields_list = []
        
        admin_code.append( "" )

        # admin.site.register()
        for model_class in model_classes:
            admin_code.append( f"admin.site.register({model_class},{model_class}Admin)" )
            
        # === 軽微な調整 ===
        # 'を"に
        admin_code  = [ c.replace("'", "\"") for c in admin_code]
        admin_code  = [ c.replace("[", "[ ") for c in admin_code]
        admin_code  = [ c.replace("]", " ]") for c in admin_code]

        # === 軽微な調整 ===


        # 書き込みするコード
        for c in admin_code:
            print(c)

    #====admin.pyの本体===========================

    #====対応するadmin.pyへ保存===================

    with open(admin_path, "a") as af: 
        for code in admin_code:
            af.write(code + "\n")

    #====対応するadmin.pyへ保存===================

