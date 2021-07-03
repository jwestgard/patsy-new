#!/bin/sh

sqlite3 /Users/westgard/Desktop/DriveToDx/$1 -csv <<END_SQL

SELECT
    a.id, 
    a.batch,
    a.sourcefile,
    a.sourceline,
    a.filename,
    a.bytes,
    a.timestamp,
    t.storagepath
FROM
    accessions a 
JOIN 
    perfect_matches p 
ON 
    p.accession_id = a.id 
JOIN 
    restores r
ON
    r.id = p.restore_id
JOIN
    transfers t
ON
    r.id = t.restore_id
WHERE
    a.batch = "$2"
;

END_SQL