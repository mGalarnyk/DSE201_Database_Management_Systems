
CREATE TABLE users 
(
	ID		SERIAL PRIMARY KEY,
	Name		TEXT NOT NULL UNIQUE,
	FB_Login	TEXT NOT NULL UNIQUE
)

CREATE TABLE videos 
(
	ID		SERIAL PRIMARY KEY,
	Title		TEXT NOT NULL, 
	URL		TEXT NOT NULL
)

CREATE TABLE sessions 
(
	ID		SERIAL PRIMARY KEY
)

CREATE TABLE friends 
(
	ID		SERIAL PRIMARY KEY,
	User		INTEGER REFERENCES users (ID) NOT NULL,
	Friend		INTEGER REFERENCES users (ID) NOT NULL
)

/*From my own youtube, I know there must be a unique combination of user and video id otherwise someone could like their own video many times and a video must be allowed to be liked by many */
CREATE TABLE like 
(
	ID		SERIAL PRIMARY KEY,
	Time		TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	User_ID		INTEGER REFERENCES users (ID),
	Video_ID	INTEGER REFERENCES videos (ID)
	UNIQUE (User_ID, Video_ID)
)

CREATE TABLE suggested_content
(
        ID              SERIAL PRIMARY KEY,
	Session_ID	INTEGER REFERENCES sessions (ID) NOT NULL,
	Video_ID	INTEGER REFERENCES videos (ID) NOT NULL
)


CREATE TABLE watch 
(
	ID		SERIAL PRIMARY KEY,
	Time		TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	User_ID		INTEGER REFERENCES users (ID),
	Video_ID	INTEGER REFERNECES videos (ID) NOT NULL
)

CREATE TABLE login 
(
	ID		SERIAL PRIMARY KEY,
	Time		TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	User_ID		INTEGER REFERENCES users (ID) UNIQUE,
	Session_ID	INTEGER REFERENCES sessions (ID) NOT NULL
)

