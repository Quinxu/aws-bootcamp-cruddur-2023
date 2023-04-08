SELECT 
  users.uuid
FROM public.users
WHERE 
  users.cognito_user_id = '{}'
LIMIT  1