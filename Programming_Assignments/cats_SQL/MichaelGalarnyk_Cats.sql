-- Query 1 “Overall Likes”: The Top-10 cat videos are the ones 
-- that have collected the highest numbers of likes, overall.

SELECT v.video_id, v.video_name, ordLikes.Likes_Overall 
FROM 
	(
        SELECT video_id, COUNT(*) Likes_Overall
        FROM cats.likes
        GROUP BY video_id
        ORDER BY Likes_Overall DESC LIMIT 10
	) ordLikes
JOIN cats.video v
ON  v.video_id = ordLikes.video_id;

-- Query 2 “Friend Likes”: The Top-10 cat videos are the ones that 
-- have collected the highest numbers of likes from the friends of X.

SELECT v.video_name, v.video_id, edith.CNT FriendLikes
FROM 
	(
	SELECT L.video_id
	  , COUNT(L.video_id) CNT
	FROM cats.user u
	    JOIN cats.friend f
	    ON  u.user_id = f.user_id
	    JOIN cats.likes L
	    ON  F.friend_id = L.user_id
	WHERE u.user_name = 'Edith1Moore'
	GROUP BY L.video_id
	ORDER BY CNT DESC LIMIT 10
	) edith
JOIN cats.video v 
ON edith.video_id = v.video_id;

-- Query 3 “Friends-of-Friends Likes”: The Top-10 cat videos are 
-- the ones that have collected the highest numbers of likes from 
-- friends and friends-of-friends.

SELECT v.video_id, v.video_name, E.CNT Distant_Likes
FROM
	(
	SELECT L.video_id, COUNT(L.video_id) CNT
	FROM CATS.USER U
	    LEFT JOIN CATS.FRIEND F
	    ON  U.user_id = F.user_id
	    LEFT JOIN CATS.FRIEND FF
	    ON  F.friend_ID = FF.user_id
	    LEFT JOIN cats.likes L
	    ON  FF.friend_id = L.user_id   
		OR F.friend_ID = L.user_ID
	WHERE USER_NAME = 'Edith1Moore'
	    AND L.user_id != u.user_id
	GROUP BY L.video_id
	ORDER BY CNT DESC LIMIT 10
	) E
JOIN cats.video v
ON  v.video_id = E.video_id;

-- Query 4 “My kind of cats”: The Top-10 cat videos 
-- are the ones that have collected the most likes from
-- users who have liked at least one cat video that was liked by X.

SELECT v.video_id, v.video_name, E.CNT Distant_Like
FROM
	(
        SELECT p2.video_id
          , COUNT(p2.like_id) CNT
        FROM cats.user u
            JOIN cats.likes p1
            ON  u.user_id = p1.user_Id
            JOIN cats.likes p2 
            ON  p1.video_id = p2.video_id
        WHERE u.user_name = 'Edith1Moore'
        GROUP BY p2.video_id
	) E
JOIN cats.video v
ON  v.video_id = E.video_id
ORDER BY Distant_Like DESC LIMIT 10;

-- Query 5  “My kind of cats – with preference 
-- (to cat aficionados that have the same tastes)”

WITH wusers AS
    (
    SELECT l2.user_id,
    log(COUNT(l2.like_id) + 1) like_weigh
    FROM cats.user u
    JOIN cats.likes l 
    ON  u.user_id = l.user_Id
    JOIN cats.likes l2
    ON  l2.video_id = l.video_id
    WHERE u.user_name = 'Edith1Moore'
    GROUP BY l2.user_id
    ),
wlikes AS
    (
    SELECT l.video_id,
    SUM(w.like_weigh) sum_weigh
    FROM cats.likes l
    JOIN wusers w
    ON l.user_id = w.user_id
    GROUP BY l.video_id
    ORDER BY sum_weigh DESC limit 10
    )
SELECT l.sum_weigh, v.video_name, v.video_id
FROM wlikes l
JOIN cats.video v
ON  l.video_id = v.video_id;