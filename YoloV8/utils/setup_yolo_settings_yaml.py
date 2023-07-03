def setup_yolo_settings_yaml(save_path="./settings.yaml"):
#     Note that this function can break depending on which Ultralytics version is out.
#     To update it just copy/paste the default settings file, and change paths to "./"

    import os
    import hashlib
    import uuid
    default_uuid = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest(),  # SHA-256 anonymized UUID hash,
#         This UUID is equal to the definition in `ultralytics/ultralytics/hub/utils.py`.
        
    file_contents = f"""
datasets_dir: "./" 
weights_dir: "./" 
runs_dir: "./" 
uuid: {default_uuid[0]}
sync: true
api_key: ''
settings_version: 0.0.3
    """.strip() + "\n"
    
    file = open(save_path, "w")
    file.write(file_contents)

    os.environ['YOLO_CONFIG_DIR'] = os.path.dirname(os.path.abspath(file.name))
    
    file.close()
    print("All done. settings.yaml path is:", os.environ['YOLO_CONFIG_DIR'])
