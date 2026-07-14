def update_order():
    chai_type  = "Adarak"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print(f"After Kitchen update ",chai_type)
    
update_order()