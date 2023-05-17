CREATE VIEW GAMES_BY_USER AS
SELECT
    g.id,
    g.title,
    g.maker,
    g.game_type_id,
    g.num_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
;

CREATE VIEW EVENTS_BY_USERS AS
SELECT
    ur.id,
    ur.first_name,
    ur.last_name,
    e.id,
    e.description,
    e.date,
    e.time
FROM levelupapi_event e
JOIN auth_user ur ON e.organizer_id = ur.id;