# Internet Fundamentals

## 1. From Client to Server

When we type `www.youtube.com` into a browser, several things happen:

1. **Client:** The browser receives the URL and starts a request to access YouTube.
2. **DNS:** The browser uses DNS to find the IP address associated with `www.youtube.com`.
3. **IP Address:** Once the IP address is found, the browser uses it to connect to Google's servers.
4. **HTTP/HTTPS:** The browser sends an HTTPS request to the server. HTTPS encrypts the communication to keep the data secure.
5. **Server:** The server processes the request and sends back the necessary files and data.
6. **Browser:** The browser loads the page. When we select a video, it requests the video data and starts playing it.

In simple terms, the client requests information, and the server responds with the data needed to display the website.

## 2. Frontend and Backend in Action

Imagine we are developing a web application for booking medical appointments.

### Frontend

The frontend is everything the user can see and interact with, such as:

- Login and registration forms.
- A calendar to select appointment dates.
- Buttons to book or cancel appointments.

**Three possible technologies:** HTML, CSS, and JavaScript (React could also be used).

### Backend

The backend handles the logic and data behind the application, including:

- Managing users and appointments.
- Checking doctor availability.
- Saving information in a database.

**Three possible technologies:** Python (FastAPI), Java (Spring Boot), and JavaScript (Node.js).

### How do they communicate?

The frontend communicates with the backend through an **API** using HTTP requests.

For example, when a user books an appointment:

1. The frontend sends a `POST` request to the API with the appointment details.
2. The backend checks if the selected time is available.
3. If everything is correct, the backend saves the appointment.
4. The backend sends an HTTP response confirming the reservation.

This process is called **Request/Response**.

## 3. REST vs SOAP vs GraphQL

| API Type | Data Format | Flexibility | Implementation Difficulty | Current Usage |
|---|---|---|---|---|
| REST | JSON/XML | Medium | Low | High |
| SOAP | XML | Low | High | Medium |
| GraphQL | JSON | High | Medium/High | High |

### Which API would be better for a modern startup?

I would choose **REST** for a startup developing an online booking system.

REST is simple to implement, easy to maintain, and widely supported by modern frameworks like FastAPI and Spring Boot.

It also works well with common operations such as creating, updating, viewing, and deleting reservations.

GraphQL could be a good alternative for more complex applications, but REST would be enough for most startup projects.

## 4. Exploring APIs with Postman

### 4.1 API Selection
- **API Name:** JSONPlaceholder
- **Description:** JSONPlaceholder is a free public REST API designed for testing and learning. It provides fake resources such as posts, users, comments, albums, photos, and todos.

### 4.2 Postman Configuration
- **Collection Name:** JSONPlaceholder
- **Requests Added:**
  - GET - Get Posts
  - POST - Create Post
  - PUT - Update Post
  - DELETE - Delete Post

### 4.3 Execution and Analysis

| Request | Method | Endpoint | Status Code | Notes |
|-----------|--------|----------|-------------------|-------|
| Get Posts | GET | `/posts` | 200 OK | Returns a list of posts in JSON format. |
| Create Post | POST | `/posts` | 201 Created | Simulates the creation of a new post. |
| Update Post | PUT | `/posts/1` | 200 OK | Simulates updating the post with ID 1. |
| Delete Post | DELETE | `/posts/1` | 200 OK | Simulates deleting the post with ID 1. |

### 4.4 Technical Explanation

#### Get Posts
- **HTTP Method:** GET
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Parameters / Body:** No parameters or body are required.
- **Response Description:** Returns an array containing the available posts. Each post contains properties such as `userId`, `id`, `title`, and `body`.

Example response:

```json
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
```

#### Create Post
- **HTTP Method:** POST
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Parameters / Body:**

```json
{
    "title": "Learning APIs",
    "body": "Testing POST requests with Postman",
    "userId": 1
}
```

- **Response Description:** Returns the information sent in the request along with a generated `id`. The API responds with status code `201 Created`.

Example response:

```json
{
    "title": "Learning APIs",
    "body": "Testing POST requests with Postman",
    "userId": 1,
    "id": 101
}
```

#### Update Post
- **HTTP Method:** PUT
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Parameters / Body:**

```json
{
    "id": 1,
    "title": "Learning REST APIs",
    "body": "Testing PUT requests with Postman",
    "userId": 1
}
```

- **Response Description:** Returns the post with the updated information. The API responds with status code `200 OK`.

#### Delete Post
- **HTTP Method:** DELETE
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Parameters / Body:** No body is required.
- **Response Description:** Simulates deleting the post with ID `1`. The API responds with status code `200 OK` and an empty JSON object.

```json
{}
```

**What did you learn from the process?**

During this exercise, I learned how to use Postman to interact with a REST API and how the main HTTP methods work. I used GET to retrieve information, POST to send and create data, PUT to update existing data, and DELETE to remove data.

I also learned how to inspect HTTP status codes, JSON response bodies, endpoints, and headers. This exercise helped me understand how clients communicate with servers through HTTP requests and how REST APIs can be tested using Postman.

## 5. Final Reflection

During this practice, I learned how APIs allow different applications to communicate and exchange information. I also understood better how methods like GET, POST, PUT, and DELETE are used to request, create, modify, or remove data.

Postman made this much easier to understand because I could see the requests and responses directly. Instead of only reading about how APIs work, I was able to experiment with them and see how the server responds to different requests.