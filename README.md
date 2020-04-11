# group-flip
Flask/React social flip book game utilizing docker/docker-compose and postgres db.
## Setup
1. Copy example.env to .env and change env variables.
2. Run `docker-compose build && docker-compose up`

## Testing
1. Run `docker-compose up`
2. Open a new terminal tab and run `docker exec -it {APP_NAME}-client bash`
3. Run `npm run test`
4. After tests pass, run `exit` and exec into the backend `docker exec -it {APP_NAME}-server bash`
5. Run `nose2 -v` to run all the python unit tests