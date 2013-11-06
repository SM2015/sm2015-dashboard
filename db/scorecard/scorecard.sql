--
-- Name: milestone; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE scorecard (
    id integer NOT NULL,
    milestone character varying(1000) NOT NULL,
    unit character varying(1000) NOT NULL,
    quarter character varying(100) NOT NULL,
    status character varying(100) NOT NULL
);


ALTER TABLE public.scorecard OWNER TO postgres;

--
-- Name: milestone_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE scorecard_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.scorecard_id_seq OWNER TO postgres;

ALTER SEQUENCE scorecard_id_seq OWNED BY scorecard.id;

ALTER TABLE ONLY scorecard ALTER COLUMN id SET DEFAULT nextval('scorecard_id_seq'::regclass);

SELECT pg_catalog.setval('scorecard_id_seq', 1, false);

ALTER TABLE ONLY scorecard
    ADD CONSTRAINT scorecard_pkey PRIMARY KEY (id);