# Learnings
Documenting my learnings.

# Day-1 23/06/2026 

## HTTP
- HTTP- Hyper Text Transfer protocol
- Communication b/w web servers and clients 
- HTTP Requests/Responses 
- Loading pages. form submit, Ajax calls, fetch requests

## HTTP is stateless 
- Every req is completely independent( doesnt remember anything about the previous transaction)
- Each req is a single transaction
- programming, local storage, cookies, Sessions are used to create enhanced user experiences

## HTTPS ??

- Hyper Text Transfer Protocol Secure 
- Data sent back and forth is encrypted 
- SSL / TLS 
- To send sensitive info like credit card details or personals 
- Install Certificate on web host

# HTTPS Methods
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
## GET 
- Everytime we are visiting a website we are using get request to the server 
## POST
- When we are adding something to the server (blogs,forms)
## PUT
- Update data which was already on the server
## Delete 
- Just delete data from Server

  
## Header - request headers, response headers and general headers 
<img width="677" height="357" alt="image" src="https://github.com/user-attachments/assets/69b61035-ea66-4a2a-a827-15be0eefbf81" />
- header data is hidden to save from hackers  
## HTTP Status codes
- 100 to 500
- The HTTP 302 Found redirection response status code indicates that the requested resource has been temporarily moved to the URL in the Location header.
- - A browser receiving this status will automatically request the resource at the URL in the Location header, redirecting the user to the new page.
<img width="834" height="468" alt="image" src="https://github.com/user-attachments/assets/65f8c171-bb60-4ce2-ac91-63e3a4bd52ee" />

## HTTP/2
- Faster, efficient and secure
- Reduces latency
- Respond with more data
- gets styles and scripts at one go 
<img width="330" height="357" alt="image" src="https://github.com/user-attachments/assets/53e45746-6c29-4f1d-8bca-6f0962c2afaf" />

# REST API

- Representational State Transfer
- Client ---HTTP---> Server

# Day 2 24/06/2026
# Fast API
## Installation
- pip install "fastapi[standard]"
- To run
- - fastapi dev main.py
    








