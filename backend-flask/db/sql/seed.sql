-- this file was manually created
INSERT INTO public.users (display_name, handle, email, cognito_user_id)
VALUES
  ('Quin Xu', 'quinxu', 'quinxu@hotmail.com', 'MOCK'),
  ('Andrew Brown', 'andrewbrown', 'andrew@exampro.co' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'quinxu' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )