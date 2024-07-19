# Following System API

This project is a following system implemented using Django and Django REST Framework.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/following-system.git
   cd following-system
   ```
2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
5. **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```
6. **Run the development server:**

    ```bash
    python manage.py runserver
   ```

## API Documentation
### Follow API
#### Endpoint: POST /api/follow/
#### Request Data:

`{
  "user_id": 1,
  "follower_id": 2
}`

#### Response:
`{
  "detail": "Followed successfully"
}`

### Unfollow API
#### Endpoint: POST /api/unfollow/
#### Request Data:
`{
  "user_id": 1,
  "follower_id": 2
}`
#### Response:
`{
  "detail": "Unfollowed successfully"
}`

### Daily Follower Count API
#### Endpoint: GET /api/follower-count/<user_id>/
#### Example Request: GET /api/follower-count/1/
#### Response:
`{
  "user_id": 1,
  "username": "user1",
  "follower_count": 5
}`

### Common Followers API
#### Endpoint: GET /api/common-followers/<user1_id>/<user2_id>/
#### Example Request: GET /api/common-followers/1/2/
#### Response:
`[
  {
    "id": 2,
    "username": "user2"
  },
  {
    "id": 3,
    "username": "user3"
  }
]`



## Swagger UI: http://127.0.0.1:8000/swagger/
## ReDoc: http://127.0.0.1:8000/redoc/