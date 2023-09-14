SELECT
  b.uuid,
  b.handle,
  b.display_name,
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json)
    SELECT a.uuid, b.display_name, b.handle, a.message, a.created_at, a.expires_at
    FROM public.activities a 
    where b.uuid = a.uuid
    ORDER BY a.created_at DESC
    limit 40
 ) array_row) as activities
FROM public.users b
WHERE 
  b.handle = %(handle)s