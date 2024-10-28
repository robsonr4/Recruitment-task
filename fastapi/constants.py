LOGIN_POST_DESC = """# Login user 
    
    BODY
    ----
    username: str
        User's username
    password: str
        User's password
    
    RETURNS
    -------
    message: str
        Login successful
    
    Raises:
    HTTPException: 404
        The user does not exist
    HTTPException: 401
        The password is incorrect
    """