--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: infomilestone; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE infomilestone (
    id integer NOT NULL,
    country character varying(300),
    updated character varying(30),
    executed character varying(30),
    planned character varying(30),
    alerts text,
    expended character varying(30),
    pep character varying(30),
    progression character varying(300),
    recommendation text
);


ALTER TABLE public.infomilestone OWNER TO postgres;

--
-- Name: infomilestone_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE infomilestone_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.infomilestone_id_seq OWNER TO postgres;

--
-- Name: infomilestone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE infomilestone_id_seq OWNED BY infomilestone.id;


--
-- Name: member; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE member (
    mem_id integer NOT NULL,
    username character(30) NOT NULL,
    password character varying(30) NOT NULL,
    fname character varying(30) NOT NULL,
    lname character varying(30) NOT NULL,
    address character varying(100) NOT NULL,
    contact character varying(30) NOT NULL,
    picture character varying(100) NOT NULL,
    gender character varying(10) NOT NULL,
    activation character varying(40),
    level character varying(10),
    countries character varying(300)
);


ALTER TABLE public.member OWNER TO postgres;

--
-- Name: member_mem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE member_mem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.member_mem_id_seq OWNER TO postgres;

--
-- Name: member_mem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE member_mem_id_seq OWNED BY member.mem_id;


--
-- Name: milestone; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE milestone (
    id integer NOT NULL,
    country character varying(1000) NOT NULL,
    indicator character varying(1000) NOT NULL,
    milestone character varying(1000) NOT NULL,
    quarter character varying(100) NOT NULL,
    audience character varying(100) NOT NULL,
    status character varying(100) NOT NULL,
    alerts character varying(1000),
    recommendation character varying(1000),
    agreements character varying(1000),
    activitypoa character varying(1000)
);


ALTER TABLE public.milestone OWNER TO postgres;

--
-- Name: milestone_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE milestone_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.milestone_id_seq OWNER TO postgres;

--
-- Name: milestone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE milestone_id_seq OWNED BY milestone.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY infomilestone ALTER COLUMN id SET DEFAULT nextval('infomilestone_id_seq'::regclass);


--
-- Name: mem_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY member ALTER COLUMN mem_id SET DEFAULT nextval('member_mem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY milestone ALTER COLUMN id SET DEFAULT nextval('milestone_id_seq'::regclass);


--
-- Data for Name: infomilestone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY infomilestone (id, country, updated, executed, planned, alerts, expended, pep, progression, recommendation) FROM stdin;
1	Belize	15 de Julio de 2013	15%	5%	Sed egestas in diam lacus phasellus nascetur diam, integer, platea? Lundium eros ultrices sed, eu penatibus pid eu turpis ac porttitor ut! Sed porttitor, tempor integer! Ac, aliquam platea tortor? Tempor massa ac scelerisque natoque montes. Mus vut placerat parturient, vel elit et risus, adipiscing vel sit eu, a, adipiscing, nec! Auctor in nec sed dolor, cras egestas ac porttitor, magna integer mid porttitor sit rhoncus aenean quis elementum eu! Dapibus lorem lorem velit sed tincidunt, nascetur tincidunt phasellus ac aenean adipiscing mus magna! Enim ac augue, cum porttitor nunc? Dapibus dignissim et facilisis urna eu, vel odio natoque ut. Elementum odio cum ac lorem! Mauris et hac. Augue hac, dis, placerat? Penatibus porttitor, vel diam quis auctor in est.	$1000	13	2% ejecutado y 5% comprometido para pagos hasta el 31 de Julio	Sed egestas in diam lacus phasellus nascetur diam, integer, platea? Lundium eros ultrices sed, eu penatibus pid eu turpis ac porttitor ut! Sed porttitor, tempor integer! Ac, aliquam platea tortor? Tempor massa ac scelerisque natoque montes. Mus vut placerat parturient, vel elit et risus, adipiscing vel sit eu, a, adipiscing, nec! Auctor in nec sed dolor, cras egestas ac porttitor, magna integer mid porttitor sit rhoncus aenean quis elementum eu! Dapibus lorem lorem velit sed tincidunt, nascetur tincidunt phasellus ac aenean adipiscing mus magna! Enim ac augue, cum porttitor nunc? Dapibus dignissim et facilisis urna eu, vel odio natoque ut. Elementum odio cum ac lorem! Mauris et hac. Augue hac, dis, placerat? Penatibus porttitor, vel diam quis auctor in est.
2	Nicaragua	15 de Julio de 2013	14%	11%	Rhoncus. Eu ultricies augue auctor. Adipiscing placerat? Lorem adipiscing. Pulvinar turpis adipiscing aliquet porta mattis, mid nec, egestas ut? Etiam! Pid enim in in augue mid integer ultricies. Ultricies enim enim, ac pellentesque eros rhoncus mauris cras rhoncus rhoncus! Et enim diam enim montes est hac tristique duis nec, et? Adipiscing proin proin, tortor elementum placerat aenean adipiscing scelerisque? Sociis tristique natoque, nec ut non elementum, lacus nunc aenean nisi turpis sagittis a pellentesque nec? Pulvinar aliquam, rhoncus placerat pulvinar nec placerat vut nunc ut pulvinar, etiam porta scelerisque? Turpis vut tincidunt aenean magna, mauris mattis elit proin lorem habitasse diam sit nisi! Scelerisque nisi lorem. Pellentesque cum tortor cras. Porttitor. Facilisis purus velit lectus platea pulvinar turpis porta.	11%	11%	2% ejecutado	Rhoncus. Eu ultricies augue auctor. Adipiscing placerat? Lorem adipiscing. Pulvinar turpis adipiscing aliquet porta mattis, mid nec, egestas ut? Etiam! Pid enim in in augue mid integer ultricies. Ultricies enim enim, ac pellentesque eros rhoncus mauris cras rhoncus rhoncus! Et enim diam enim montes est hac tristique duis nec, et? Adipiscing proin proin, tortor elementum placerat aenean adipiscing scelerisque? Sociis tristique natoque, nec ut non elementum, lacus nunc aenean nisi turpis sagittis a pellentesque nec? Pulvinar aliquam, rhoncus placerat pulvinar nec placerat vut nunc ut pulvinar, etiam porta scelerisque? Turpis vut tincidunt aenean magna, mauris mattis elit proin lorem habitasse diam sit nisi! Scelerisque nisi lorem. Pellentesque cum tortor cras. Porttitor. Facilisis purus velit lectus platea pulvinar turpis porta.
\.


--
-- Name: infomilestone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('infomilestone_id_seq', 2, true);


--
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY member (mem_id, username, password, fname, lname, address, contact, picture, gender, activation, level, countries) FROM stdin;
16	javier@jzferreira.com         	jav12suz	Javier	Ferreira					\N	admin	Belize,Costa Rica,El Salvador,Honduras,Guatemala,Nicaragua
3	fabianoc@acm.org              	db	Fabiano	Cruz	1325 15TH	+12029579543		male		admin	\N
4	admin                         	dashboard	Admin	Dashboard	panama					admin	\N
5	zambrano.ferreira@gmail.com   	dashboard	Javier	Zambrano						admin	Nicaragua
\.


--
-- Name: member_mem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('member_mem_id_seq', 16, true);


--
-- Data for Name: milestone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY milestone (id, country, indicator, milestone, quarter, audience, status, alerts, recommendation, agreements, activitypoa) FROM stdin;
46	El Salvador	Número de ECOS Familiares y Especializados conformados	100% de los ECOS Familiares y Especializados conformados	T1 2013	Donantes	cumplida	\N	\N	\N	\N
47	El Salvador	Revisión de la política nacional para la distribución de micronutrientes en polvo en niños de 6 a 23 meses	1ra recepción de micronutrientes en polvo en niños de 6 a 23 meses	T3 2013	Donantes	 	\N	\N	\N	\N
48	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Columna de Fecha de Ultima Regla (FUR) incluída en el tablero de control de promotores 	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
49	El Salvador	Porcentaje de niños menores de 1 año inscritos en el sistema que han sido inscritos antes de los 8 días	Contrato firmado enviado al BID para contratación de los Equpios Comunitarios de Salud (ECOS)	T2 2013	Donantes	 	\N	\N	\N	\N
50	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención infantil	Contrato firmado enviado al BID para los insumos necesarios para la atención infantil	T2 2013	Donantes	 	\N	\N	\N	\N
51	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Contrato firmado enviado al BID para los insumos necesarios para la atención prenatal	T2 2013	Donantes	 	\N	\N	\N	\N
52	El Salvador	Número de unidades comunitarias de salud familiar que cuentan con refrigerador o caja fría para la conservación adecuada de vacunas	Contrato firmado enviado al BID para refrigeradores o caja frías para la conservación adecuada de vacunas	T2 2013	Donantes	 	\N	\N	\N	\N
53	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Convenio UES MINSAL firmado para construcción de Unidades Comunitarias de Salud Familiar (UCSF)	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
54	El Salvador	Porcentaje de niños menores de 1 año inscritos en el sistema que han sido inscritos antes de los 8 días	Convenio UES MINSAL firmado para construcción de Unidades Comunitarias de Salud Familiar (UCSF)	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
55	El Salvador	Número de unidades comunitarias de salud con abastecimiento de  4 métodos modernos de planificación familiar (inyectables, barrera, orales, DIU)	Distribucion anticonceptivos a unidades comunitarias de salud 	T3 2013	Donantes	 	\N	\N	\N	\N
56	El Salvador	Porcentaje de niños menores de 1 año inscritos en el sistema que han sido inscritos antes de los 8 días	Distribucion de equipos a Unidades Comunitaros de Salud Familiar (UCSF)	T3 2013	Donantes	 	\N	\N	\N	\N
57	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención infantil	Distribucion de equipos a Unidades Comunitaros de Salud Familiar (UCSF)  para la atención infantil	T3 2013	Donantes	 	\N	\N	\N	\N
58	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Distribucion de equipos a Unidades Comunitaros de Salud Familiar (UCSF) para insumos necesarios para la atención prenatal	T3 2013	Donantes	 	\N	\N	\N	\N
59	El Salvador	Número de unidades comunitarias de salud familiar que cuentan con refrigerador o caja fría para la conservación adecuada de vacunas	Distribucion de refrigeradores o caja frías para la conservación adecuada de vacunas a Unidades Comunitaros de Salud Familiar (UCSF) 	T3 2013	Donantes	 	\N	\N	\N	\N
33	Nicaragua	Parteras y Brigadistas entrenados en  Estrategia Comunitaria de Métodos Anticonceptivos (ECMAC)  y con constancia de entrenamiento emitida por el MINSA de acuerdo con la programación y al momento de la medición	Contratación de Facilitadores de Gestión Comunitaria en los 19 Municipios	T1 2013	Donantes	Completado	\N	\N	\N	\N
35	Nicaragua	Centros de Salud Municipales que implementan el mecanismo para la entrega de certificados de subsidio de transporte y estancia para y embarazadas, establecido en el Reglamento Operativo	Selección final de comunidades para entrega de  vales a embarazadas	T1 2013	Donantes	Retrasado	\N	\N	\N	\N
34	Nicaragua	Mujeres embarazadas que se albergan en las Casas Maternas, que tuvieron acceso a materiales educativos y a actividades de capacitación reportadas al centro de salud de acuerdo a los lineamientos de supervisión y monitoreo contenidos en el Reglamento Operativo 	Inicio del proceso de selección de capacitadores para las parteras por actividades educativas en las Casas Maternas	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
60	El Salvador	Inclusión en la norma de la dosis adecuada de zinc terapéutico para tratamiento de la diarrea en niños menores de 5 años (20 mg de zinc por 10-14 días en cada episodio de diarrea)	El dosis adecuada de zinc terapéutico para tratamiento de la diarrea en niños menores de 5 años incluida en la norma	T1 2013	Donantes	cumplida	\N	\N	\N	\N
61	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Entrega de medicamentos en almacén para la atención prenatal	T3 2013	Donantes	 	\N	\N	\N	\N
62	El Salvador	Revisión de la política nacional para la distribución de micronutrientes en polvo en niños de 6 a 23 meses	Envío de contrato firmado al BID para micronutrientes en polvo en niños de 6 a 23 meses	T2 2013	Donantes	 	\N	\N	\N	\N
63	El Salvador	Número de unidades comunitarias de salud con abastecimiento de  4 métodos modernos de planificación familiar (inyectables, barrera, orales, DIU)	Envío de formulario a UNFPA para  el compra de los 4 métodos modernos de planificación familiar	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
38	Nicaragua	Mujeres embarazadas que se albergan en las Casas Maternas, que tuvieron acceso a materiales educativos y a actividades de capacitación reportadas al centro de salud de acuerdo a los lineamientos de supervisión y monitoreo contenidos en el Reglamento Operativo 	Recepción y pago de maletas pedagógicas para las parteras por actividades educativas en las Casas Maternas	T2 2013	Donantes	En Proceso	s	s	s	s
39	Nicaragua	Auxiliares de enfermería y agentes comunitarios (parteras y brigadistas de salud) entrenados en el manejo comunitario del neonato enfermo y con constancia de entrenamiento emitida por el MINSA de acuerdo con la programación y al momento de la medición	Negociación de la propuesta de capacitación de auxiliares de enfermería y agentes comunitarios (parteras y brigadistas de salud) entrenados en el manejo comunitario del neonato enfermo	T2 2013	Donantes	En Proceso				
36	Belize	Centros de Salud Municipales que implementan el mecanismo para la entrega de certificados de subsidio de transporte y estancia para y embarazadas, establecido en el Reglamento Operativo	Entrega del primer subsidio de transporte y estancia para y embarazadas	T1 2013	Donantes	Retrasado	\N	\N	\N	\N
64	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Incorporacion temas planificacion y nutricion en capacitacion	T3 2013	Donantes	 	\N	\N	\N	\N
65	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Inicio de primer modulo de capacitacion de Equipos Comunitarios de Salud (ECOS)	T3 2013	Donantes	 	\N	\N	\N	\N
66	El Salvador	Porcentaje de niños menores de 1 año inscritos en el sistema que han sido inscritos antes de los 8 días	Inicio de primer modulo de capacitacion de Equipos Comunitarios de Salud (ECOS)	T3 2013	Donantes	 	\N	\N	\N	\N
67	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención infantil	Licitación publicado para los insumos necesarios para la atención infantil para los Unidades Comunitaros de Salud Familiar (UCSF)	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
68	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Licitación publicado para los insumos necesarios para la atención prenatal para los Unidades Comunitaros de Salud Familiar (UCSF)	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
69	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención infantil	No objeción a informe evaluación ofertas para los insumos necesarios para la atención infantil	T2 2013	Donantes	 	\N	\N	\N	\N
70	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	No objeción a informe evaluación ofertas para los insumos necesarios para la atención prenatal	T2 2013	Donantes	 	\N	\N	\N	\N
71	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención infantil	No objecion del BID a adendas a contratos PRIDES para la compra de equipo médico	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
72	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	No objecion del BID a adendas a contratos PRIDES para la compra de equipo médico	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
73	El Salvador	Porcentaje de niños menores de 1 año inscritos en el sistema que han sido inscritos antes de los 8 días	No objecion del BID a adendas a contratos PRIDES para la compra de equipo médico	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
74	El Salvador	Número de unidades comunitarias de salud familiar que cuentan con refrigerador o caja fría para la conservación adecuada de vacunas	No objecion del BID a contratacion directa para compra de los refrigeradores o caja frías para la conservación adecuada de vacunas	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
75	El Salvador	Número de unidades comunitarias de salud con abastecimiento de  4 métodos modernos de planificación familiar (inyectables, barrera, orales, DIU)	Recepción anticonceptivos para los unidades comunitarias de salud	T2 2013	Donantes	 	\N	\N	\N	\N
76	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Recepción de informe de evaluación de los ofertas para medicamentos necesarios para la atención prenatal	T2 2013	Donantes	En Proceso	\N	\N	\N	\N
77	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	recepción de informe de evaluación de ofertas de vehiculos	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
78	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Recepción de insumos médicos en almacén para insumos necesarios para la atención prenatal	T3 2013	Donantes	 	\N	\N	\N	\N
79	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención infantil	Recepción de insumos médicos en almacén para la atención infantil	T3 2013	Donantes	 	\N	\N	\N	\N
80	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Recepción de vehículos para aumentar la búsqueda activa de mujeres embarazadas 	T2 2013	Donantes	 	\N	\N	\N	\N
81	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Revisión de cronograma de capacitacion y propuesta de inclusión de salud reproductiva y nutricion para mejorar la atención prenatal	T2 2013	Donantes	 	\N	\N	\N	\N
82	El Salvador	Porcentaje de mujeres embarazadas inscritas en el registro prenatal que tuvieron un control prenatal realizado por médico o enfermera antes de las 12 semanas.	Selección de planta docente para capacitacion de Equipos Comunitarios de Salud (ECOS)	T2 2013	Donantes	 	\N	\N	\N	\N
83	El Salvador	Porcentaje de niños menores de 1 año inscritos en el sistema que han sido inscritos antes de los 8 días	Selección de planta docente para capacitacion de Equipos Comunitarios de Salud (ECOS)	T2 2013	Donantes	 	\N	\N	\N	\N
84	El Salvador	Revisión de la política nacional para la distribución de micronutrientes en polvo en niños de 6 a 23 meses	Solicitud de compra para no objeción del banco para el compra de micronutrientes en polvo en niños de 6 a 23 meses	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
85	El Salvador	Número de unidades comunitarias de salud que cuentan con los insumos necesarios para la atención prenatal	Suscripción de contrato de medicamentos necesarios para la atención prenatal	T2 2013	Donantes	 	\N	\N	\N	\N
30	Nicaragua	Unidades de salud municipales (Centros de Salud Familiar) que suscriben Acuerdos Sociales para la Salud y el Bienestar de la Comunidad con los comités de salud comunitaria y realizan informes de seguimiento del mismo de acuerdo a los lineamientos de supervisión y monitoreo contenidos en el Reglamento Operativa	Comunidades selecionadas para suscripción de Acuerdos Sociales Comunitarios	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
31	Nicaragua	Unidades de salud municipales (Centros de Salud Familiar) que suscriben Acuerdos Sociales para la Salud y el Bienestar de la Comunidad con los comités de salud comunitaria y realizan informes de seguimiento del mismo de acuerdo a los lineamientos de supervisión y monitoreo contenidos en el Reglamento Operativa	Suscripción de Acuerdos Sociales para la Salud y el Bienestar de la Comunidad con los comités de salud comunitaria	T1 2013	Donantes	Cumplido	\N	\N	\N	\N
37	Nicaragua	Auxiliares de enfermería y agentes comunitarios (parteras y brigadistas de salud) entrenados en el manejo comunitario del neonato enfermo y con constancia de entrenamiento emitida por el MINSA de acuerdo con la programación y al momento de la medición	Protocolo del manejo comunitario del neonato enfermo aprobado	T1 2013	Donantes	Retrasado	teste	teste	teste	teste
\.


--
-- Name: milestone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('milestone_id_seq', 1, false);


--
-- Name: infomilestone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY infomilestone
    ADD CONSTRAINT infomilestone_pkey PRIMARY KEY (id);


--
-- Name: member_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY member
    ADD CONSTRAINT member_pkey PRIMARY KEY (mem_id);


--
-- Name: milestone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY milestone
    ADD CONSTRAINT milestone_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

