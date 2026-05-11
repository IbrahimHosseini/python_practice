# main.py


from fastapi import FastAPI, HTTPException, status
from models import CreateUserRequest, UserResponse, ErrorResponse

app = FastAPI()



# Fake db
users_db = {
	1: {"id": 1, "name": "Ali", "age": 25, "email": "ali@gmail.com"},
	2: {"id": 2, "name": "Hassan", "age": 24, "email": "hassan@gmail.com"},
}

next_id = 3


# ============ GET user ============
@app.get("/users{user_id}", response_model = UserResponse)
def get_user(user_id: int):
	"""
	user_id => from path param
	if user exist => 200 + data
	if not => 404
	"""

	if user_id not in users_db:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND,
			detail = {"code": "USER_NOT_FOUND", "message": "user not found"}
		)

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


# ============ DELETE user ============
@app.delete("/users/{user_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
	"""
	if user exist => 204 + no content/body
	if not => 404
	"""

	if user_id not in users_db:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND,
			detail = {"code": "USER_NOT_FOUND", "message": "user not found"}
		)

	del users_db[user_id]

# ============ Update user ============
@app.put("/users/{user_id}/update")
def update_user(user_id: int, user: CreateUserRequest):


	# check user is exist
	if user_id not in users_db:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND,
			detail = {"code": "USER_NOT_FOUND", "message": "user not found"}
		)

	users_db[user_id] = {**user.dict(), "id": user_id}

	return users_db[user_id]


# ============ Update user ============
@app.patch("/users/{user_id}/update")
def update_user_age(user_id: int, updates: dict):

	# check user is exist
	if user_id not in users_db:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND,
			detail = {"code": "USER_NOT_FOUND", "message": "user not found"}
		)

	users_db[user_id].update(updates)
	return users_db[user_id]
































