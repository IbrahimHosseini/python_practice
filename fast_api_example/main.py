# main.py


from fastapi import FastAPI, HTTPException, status, Depends
from models import CreateUserRequest, UserResponse, UpdateUserRequest, ErrorResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse 


app = FastAPI()



# Fake db
users_db = {
	1: {"id": 1, "name": "Ali", "age": 25, "email": "ali@gmail.com"},
	2: {"id": 2, "name": "Hassan", "age": 24, "email": "hassan@gmail.com"},
}

next_id = 3

# ============ Error Exception Handler============
@app.exception_handler(RequestValidationError)
async def validation_exception_havdler(request, exc):
	errors = []

	for error in exc.errors():
		field = error["loc"][-1]
		msg = error["msg"]
		errors.append({"field": field,
    		"message": f"{field}: {msg}"})

	return JSONResponse(
		status_code=status.HTTP_400_BAD_REQUEST,
		content={
			"code":"VALIDATION_ERROR",
			"message":"request not valid",
			"errors":errors
		}
	)

# ============ Dependencies ============
def check_user_exist(user_id: int):
	if user_id not in users_db:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND,
			detail = {"code": "USER_NOT_FOUND", "message": "user not found"}
		)

	return user_id


# ============ GET users ============
@app.get("/users")
def list_users(age: int = None, skip: int = 0, limit: int = 10):

	result = list(users_db.values())

	if age is not None:
		result = [u for u in result if u["age"] == age]

	return result[skip:skip+limit]

# ============ GET by ID ============
@app.get("/users/{user_id}", response_model = UserResponse)
def get_user(user_id: int, user_exist = Depends(check_user_exist)):
	return users_db[user_id]


# ============ POST user ============
@app.post("/users", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
def create_user(user: CreateUserRequest):
	"""
	user: from request body
	pydantic validation
	201: created successfully
	"""

	global next_id

	# validation
	if user.age < 0 or user.age > 150:
		raise HTTPException(
			status_code = status.HTTP_400_BAD_REQUEST,
			detail = {"code": "INVALID_AGE", "message": "The age have to between 0 - 150"}
		)

	new_user = {
		"id": next_id,
		"name": user.name,
		"age": user.age,
		"email": user.email,
	}

	users_db[next_id] = new_user
	next_id += 1

	return new_user


# ============ PUT Update ============
@app.put("/users/{user_id}", response_model = UserResponse)
def update_user(user_id: int, user: CreateUserRequest, user_exist = Depends(check_user_exist)):

	users_db[user_id] = {**user.dict(), "id": user_id}

	return users_db[user_id]


# ============ PATCH Update ============
@app.patch("/users/{user_id}", response_model = UserResponse)
def partial_update_user(user_id: int, updates: UpdateUserRequest, user_exist = Depends(check_user_exist)):

	user_data = updates.dict(exclude_unset = True)
	users_db[user_id].update(user_data)

	return users_db[user_id]


# ============ DELETE user ============
@app.delete("/users/{user_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, user_exist = Depends(check_user_exist)):
	del users_db[user_id]




























