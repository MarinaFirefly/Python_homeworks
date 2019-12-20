--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

-- Started on 2019-12-10 16:27:15

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16419)
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    name text NOT NULL,
    diet boolean,
    easiness boolean,
    "time" integer
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16417)
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_id_seq OWNER TO postgres;

--
-- TOC entry 2838 (class 0 OID 0)
-- Dependencies: 202
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- TOC entry 206 (class 1259 OID 16455)
-- Name: igr_for_course; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.igr_for_course (
    id_course integer,
    id_ingr integer,
    quantity numeric
);


ALTER TABLE public.igr_for_course OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16428)
-- Name: ingredients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ingredients (
    id integer NOT NULL,
    name text NOT NULL,
    price_per_kg integer
);


ALTER TABLE public.ingredients OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16426)
-- Name: ingredients_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ingredients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingredients_id_seq OWNER TO postgres;

--
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 204
-- Name: ingredients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ingredients_id_seq OWNED BY public.ingredients.id;


--
-- TOC entry 2700 (class 2604 OID 16435)
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- TOC entry 2701 (class 2604 OID 16436)
-- Name: ingredients id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ingredients ALTER COLUMN id SET DEFAULT nextval('public.ingredients_id_seq'::regclass);


--
-- TOC entry 2829 (class 0 OID 16419)
-- Dependencies: 203
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (id, name, diet, easiness, "time") FROM stdin;
1	omelette	t	t	15
2	soup with meat and pasta	t	t	90
3	pasta with sausages	f	t	30
4	borshch	f	f	90
5	fritters	f	t	40
\.


--
-- TOC entry 2832 (class 0 OID 16455)
-- Dependencies: 206
-- Data for Name: igr_for_course; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.igr_for_course (id_course, id_ingr, quantity) FROM stdin;
1	1	0.3
1	2	0.05
1	3	0.005
1	4	0.1
1	10	0.03
1	20	0.03
3	3	0.005
3	4	0.1
3	8	0.015
3	9	0.4
3	10	0.05
3	11	0.4
3	14	0.05
3	20	0.03
2	3	0.01
2	4	0.1
2	5	0.5
2	6	0.2
2	7	0.15
2	8	0.15
2	10	0.05
2	14	0.05
2	20	0.03
4	3	0.01
4	4	0.1
4	5	0.5
4	6	0.2
4	7	0.15
4	8	0.15
4	10	0.05
4	12	0.2
4	13	0.3
4	14	0.05
4	18	0.1
4	19	0.01
4	20	0.03
5	1	0.2
5	3	0.005
5	15	0.25
5	16	0.2
5	17	0.05
5	19	0.05
5	20	0.05
\.


--
-- TOC entry 2831 (class 0 OID 16428)
-- Dependencies: 205
-- Data for Name: ingredients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ingredients (id, name, price_per_kg) FROM stdin;
1	eggs	25
2	milk	20
3	salt	10
4	pepper	10
5	meat	10
6	potatoes	20
7	carrot	10
8	onion	10
9	pasta	40
10	greens	200
11	sausages	200
12	beet	20
13	cabage	20
14	garlic	100
15	flour	20
16	kefir	20
17	soda	20
18	souce from tomatoes	40
19	sugar	20
20	oil	30
\.


--
-- TOC entry 2840 (class 0 OID 0)
-- Dependencies: 202
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_id_seq', 5, true);


--
-- TOC entry 2841 (class 0 OID 0)
-- Dependencies: 204
-- Name: ingredients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ingredients_id_seq', 15, true);


-- Completed on 2019-12-10 16:27:15

--
-- PostgreSQL database dump complete
--

