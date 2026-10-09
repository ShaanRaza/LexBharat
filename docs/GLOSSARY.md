# Glossary

Every tool and term, in plain words. From the Tech Stack's glossary.

## The building blocks

| Term | What it is | Its job here |
|---|---|---|
| **Firebase** | A Google service for login | The security guard at the door: sign-in, passwords, confirming who each user is. Knows nothing about what they do inside |
| **PostgreSQL** | A database: organised tables | Users, plans, usage counts, chats, upload records and the Supreme Court text |
| **Qdrant** | A search database for meaning | Finds judgments and sections that match the *idea* of a question, not just its words |
| **Redis** | Very fast short-term memory | The waiting list of upload jobs, and saved answers to repeated questions |
| **Amazon S3** | Online file storage | Uploaded files and backups, encrypted |
| **AWS EC2** | A computer rented in Amazon's data centre | The one server in Mumbai that runs everything |
| **Docker / Compose** | Sealed boxes holding one program with everything it needs | Starts the whole system with one command, on any computer |
| **Next.js** | A tool for building websites | The website users see on phone and laptop |
| **FastAPI** | A tool for building a backend in Python | The kitchen behind the website: takes questions, runs the pipeline, sends answers |
| **Razorpay** | An Indian payment service | UPI and card payments for Student, Pro and Chambers |
| **Voyage AI** | Turns text into numbers that capture meaning | Makes meaning-search possible, and picks the best passages (re-ranking) |
| **LiteLLM** | One plug that fits many AI models | Switch between Gemini, Claude, GPT and others by changing one setting |
| **Gemini Flash-Lite** | A cheap, fast Google model | Writes the answers in v1 |
| **Tesseract** | Free software that reads text from images | Reads scanned court documents (OCR) |
| **Sentry** | An alarm for crashes | Tells you when something breaks, and where |
| **Langfuse** | A logbook for AI calls | Records every question, answer, cost and speed |
| **GitHub / Actions** | Where code lives / a robot that tests and deploys it | Every change is tested, then put on the server automatically |
| **Jev (TypeSafe AI)** | An AI that picks one answer from a fixed list, with a confidence score, instead of writing text | The quick referee: is the question in scope, do the passages answer it, does each citation really support its sentence |

## The ideas

| Term | Plain meaning |
|---|---|
| **Frontend / backend** | The part users see / the part that does the work behind it |
| **API** | The menu of requests the website can make to the backend |
| **Pipeline** | A fixed list of steps every question goes through, always in the same order |
| **Agent** | An AI that decides its own next step. Used here to help **write code**, not to answer users |
| **Embedding / vector** | A list of numbers standing for a passage's meaning, so similar meanings sit close together |
| **Semantic search** | Search by meaning: "bail for money crimes" finds "economic offences" |
| **Keyword search / BM25** | Search by exact words: finds "Section 438" exactly |
| **Hybrid search** | Running both together and merging the results |
| **Re-ranking** | A second, more careful pass that puts the best few passages on top |
| **Chunk** | A short piece of a judgment, because a whole judgment is too long to send to the AI |
| **Citation verifier** | The checker that removes any case the AI cites that was not actually found, or that does not support what the AI said |
| **OCR** | Reading text out of a scanned image of a page |
| **Token** | A piece of a word. AI costs are counted in tokens: roughly 1,000 tokens is 750 English words |
| **Cache** | A saved copy of an answer, so a repeated question costs nothing |
| **Streaming / SSE** | The answer appears word by word instead of all at once |
| **Pre-signed URL** | A one-time upload link that lets the browser send a file straight to S3 |
| **Token (login)** | A digital pass Firebase gives a logged-in user; the backend checks it on every request |
| **Adapter** | One file that talks to one outside service, so it can be swapped without touching the rest |
| **Environment variable / config** | Settings kept outside the code, such as API keys and the model name |
| **Migration** | A numbered file recording each change to the database tables, so changes can be undone |
| **Payload** | The labels stored with each item in Qdrant — court, year, section number — used as filters |
| **Quantization** | Squeezing the vectors so they use about a quarter of the memory, with little loss in search quality |
| **Audit log** | A record of who did what and when (logins, uploads, deletions) |
| **Uptime / 99.5%** | The share of time the app is working; 99.5% allows about 3.6 hours of downtime a month |
| **Calibrated confidence** | A confidence score you can trust: when it says 80% sure, it is right about 80% of the time |
| **Threshold** | The cut-off score: above it the app goes ahead; below it, it refuses or warns |
| **Fallback** | The backup the app uses automatically when a service is down or too slow |
| **OKF (Open Knowledge Format)** | Google's standard for giving AI checked knowledge as linked Markdown files, like a small wiki |
| **RAG** | Search first, then let the AI answer using only what was found |
| **SEO / sitemap** | Making pages easy for Google to find / a list of every public page, handed to Google |
| **Share card** | The preview picture that appears when a link is shared on WhatsApp or LinkedIn |
| **DPDP** | India's Digital Personal Data Protection Act 2023 and its Rules |
| **Data fiduciary / processor** | The one who decides why data is used and is responsible for it / the one who only handles it on their behalf |
| **Launch gate** | A checklist that must all pass before the public launch; if any fails, the date moves |

## Legal shorthand

| Term | Meaning |
|---|---|
| **IPC → BNS** | Indian Penal Code → Bharatiya Nyaya Sanhita (from 1 July 2024) |
| **CrPC → BNSS** | Code of Criminal Procedure → Bharatiya Nagarik Suraksha Sanhita |
| **Evidence Act → BSA** | Indian Evidence Act → Bharatiya Sakshya Adhiniyam |
| **BCI Rule 36** | Bar Council of India rule restricting advertising and solicitation by advocates |
| **SCR** | Supreme Court Reports — a citation series |
| **`acts_india`** | The Central Acts collection in the dataset |
| **Disposition / outcome label** | The raw decision value in the data / the cleaned short label (allowed, partly allowed, dismissed, disposed of, other) |
| **`is_final_outcome`** | Whether a disposition is a final result rather than an interim order. Statistics count only these |
