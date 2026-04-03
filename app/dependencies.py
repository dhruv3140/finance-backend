from fastapi import Header, HTTPException

def require_role(allowed_roles: list[str]):
    def role_checker(x_user_role: str = Header(default="viewer")):
        if x_user_role not in allowed_roles:
            raise HTTPException(
                status_code=403, 
                detail=f"Operation not permitted. Your role: {x_user_role}. Required: {allowed_roles}"
            )
        return x_user_role
        
    return role_checker