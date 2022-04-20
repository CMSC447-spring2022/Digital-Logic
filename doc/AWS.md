# AWS Resources
## Virtual Machine: Ubuntu-1
### IP: 3.85.44.32
### Processes running: Kasm (Docker container launcher client)
### Api Documentation Examples
#### Request Container
`POST` `https://3.85.44.32/api/public/request_kasm`
```
{
    "kasm_id": "4fa42139-aef3-4c86-929a-e479cda68857",
    "status": "starting",
    "user_id": "e60a9c80289a4b3aaedb42f1d5fe8060",
    "username": "user@kasm.local",
    "session_token": "6a7e5c72-cebb-44c7-94f9-b10f296a576e",
    "kasm_url": "/#/connect/kasm/4fa42139-aef3-4c86-929a-e479cda68857/e60a9c80289a4b3aaedb42f1d5fe8060/6a7e5c72-cebb-44c7-94f9-b10f296a576e"
}
```
#### Destroy Container
`POST` `https://3.85.44.32/api/public/destroy_kasm`
```
{
    "api_key": "q7I5MJFnoX16",
    "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD",
    "user_id": "e60a9c80-289a-4b3a-aedb-42f1d5fe8060",
    "kasm_id": "4f86a3fa-efe5-4d27-9091-ff9069d5f532"
}
```
#### Get Images
`POST` `https://3.85.44.32/api/public/get_images`
```
{
     "api_key": "q7I5MJFnoX16",
     "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD"
}
```
#### Get User
`POST` `https://3.85.44.32/api/public/get_user`
```
{
    "api_key": "q7I5MJFnoX16",
    "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD",
    "target_user": {
        "user_id": "e60a9c80-289a-4b3a-aedb-42f1d5fe8060",
        "username": "user@kasm.local"
    }
}
```
#### Get Users
`POST` `https://3.85.44.32/api/public/get_users`
```
{
     "api_key": "q7I5MJFnoX16",
     "api_key_secret": "hMN3qhkcibkk1wc9US7R1QalcaPZEHiD"
}
```

### Official Api Documentation
https://kasmweb.com/docs/latest/api/developer_api.html
