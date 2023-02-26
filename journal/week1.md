# Week 1 — App Containerization

## Completed Tasks

### Created the dockerfiles for front end and back end, updated docker-compose.

### Added notifications endpoint in backend flask, and notifications related files in front end.

### Installed postgres and dynamodb-local.

## Encountered Issue

### Front end Notifications didn't show mocked data even though back end can show data in api.

### Troubleshooted it as shown in the below file

![notifications error](https://user-images.githubusercontent.com/34762029/221392470-5f17df1d-f779-4d4f-aaba-82d3da8c24c3.jpg)

suspected it was caused by not properly setting up allow_headers in CORS in app.py.
