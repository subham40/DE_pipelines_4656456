-- models/staging/stg_bikeshare_trips.sql

SELECT
    trip_id,
    subscriber_type,
    duration_minutes,
    -- Rename and standardize types
    SAFE_CAST(start_time AS TIMESTAMP) AS trip_start_at
FROM {{ source('public_bikeshare', 'bikeshare_trips') }}
WHERE trip_id IS NOT NULL