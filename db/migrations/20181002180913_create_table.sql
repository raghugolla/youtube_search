-- migrate:up

CREATE TABLE IF NOT EXISTS _bookmark
(
  bookmark_key character varying(255) NOT NULL,
  bookmark_value character varying(255),
  created_at   timestamp with time zone DEFAULT now() NOT NULL,
  updated_at   timestamp with time zone DEFAULT now() NOT NULL,
  PRIMARY KEY (bookmark_key)
);


CREATE TABLE public.user (
    id uuid NOT NULL PRIMARY KEY,
    name character varying(255) NOT NULL
);

-- migrate:down

DROP TABLE public.user ;
