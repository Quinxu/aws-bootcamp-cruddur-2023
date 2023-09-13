SELECT
  users.uuid,
  users.handle,
  users.display_name,
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json)) array_row) as activities
FROM public.users
WHERE 
  users.handle = %(handle)s