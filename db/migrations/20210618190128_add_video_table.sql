-- migrate:up
CREATE TABLE video (
    id character varying PRIMARY KEY,
    title character varying,
    description character varying,
    published_at timestamp with time zone default now() not null,
    thumbnails jsonb,
    channel_id character varying,
    channel_title character varying,
    created_at timestamp with time zone default now() not null,
    updated_at timestamp with time zone default now() not null
);

-- migrate:down

