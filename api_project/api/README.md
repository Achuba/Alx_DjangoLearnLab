# API Authentication & Permissions

## Authentication

- Token-based authentication (DRF TokenAuthentication)
- Obtain token via `/api-token-auth/` endpoint with username and password
- Include token in `Authorization` header for all requests

## Permissions

- All endpoints require authentication (`IsAuthenticated`)
- Admin users can modify content (`IsAdminUser`) if applied
- Custom permissions can be added in `permission_classes` per ViewSet
