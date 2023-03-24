SELECT 
 a.uuid, b.display_name, b.handle, a.message, a.created_at, a.expires_at
FROM public.activities a
LEFT JOIN public.users b on b.uuid = a.uuid
WHERE a.uuid = %(uuid)s