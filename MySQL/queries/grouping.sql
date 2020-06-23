
# create master table so we only need to join once
CREATE TABLE master
  AS (SELECT tag245.id AS id, tag245.$a AS title, tag100.$a AS person, tag260.$b AS publisher
        FROM tag245 INNER JOIN (tag100 INNER JOIN tag260 ON tag100.id=tag260.id) 
                ON tag245.id=tag100.id )

# create a table for groups of publications that have the same author, title, and publisher
CREATE TABLE groups
  AS (SELECT title, person, publisher, COUNT(*) AS size
	FROM master
	WHERE COUNT(*) > 1
	GROUP BY title,person,publisher
	ORDER BY COUNT(*) DESC);

# give each group an ID
ALTER TABLE groups
ADD groupid int IDENTITY(1,1) PRIMARY KEY;

# create table that has record IDs linked to group id
CREATE TABLE id_groups
AS (SELECT master.id, groups.groupid
	FROM master JOIN groups 
		ON master.title=groups.title
			AND master.person=groups.person
			AND master.publisher=groups.publisher

