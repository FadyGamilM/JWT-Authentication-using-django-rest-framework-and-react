# JWT-Authentication-using-django-rest-framework-and-react

## Technologies:
- Server-Side:
    > Django Rest-framework
    > Django Rest-framework-simple-jwt
- Client-Side
    > React.js 

## System:
- In-order for any user to visit the home page, user has to register first to get access to pair of access and refresh tokens 
- the access token has less life-time than the refresh token
- the registration API returns back to the client-side both the access and the refresh token
- after the end of the life-time of the access token, if user is still logged-in, the refresh token will be used to generate new access token and this feature is established using rollback mechanism by our API 
- after the end of the life-time of the refresh token, this specific refresh token will be blacklisted into our system so if this old refresh token is exposed for any hacker, our system is still secure.
