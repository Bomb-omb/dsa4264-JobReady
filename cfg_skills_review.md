# CFG Skills Review Report

This report reviews all `CFG` rows in `data/2025-2026_module_clean_with_prereq_skillsfuture.csv` against exact title matches in `data/skills_taxo.csv`. Decisions use three labels:

- `keep`: the taxonomy description directly matches the stated module outcomes or activities.
- `manual review`: the match is adjacent or plausible, but the module description does not support a confident keep.
- `remove`: the taxonomy description is materially off-topic or too domain-specific for the module.

## CFG1002 Career Catalyst

Original extracted skills: Programme Delivery | Business Needs Analysis | Market Specialisation | Project Plan | Strategy Execution

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Programme Delivery | Deliver learning experiences according to the profile and learning needs of the students, staff or professionals, including the provision of mentorship or coaching. | remove | The module prepares students for career planning and personal branding; it does not ask them to deliver training or mentor others. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business. | remove | The description is about personal career choices, not gathering business requirements or building a business case. |
| Market Specialisation | Apply market and industry knowledge to key service offerings as well as understand relevant laws and regulations in relevant markets to be able to customise advice to clients. | manual review | Industry awareness and specialisation choices are mentioned, but the taxonomy skill is about advising clients using market and regulatory knowledge. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools. | manual review | Students map out a career plan and university roadmap, but the module does not cover formal project planning tools or project risk management. |
| Strategy Execution | Develop and implement plans to achieve organisational and departmental strategies and goals. | manual review | Students build a personal career strategy, but the taxonomy skill is framed around executing organisational or departmental strategy. |

Proposed cleaned skills: None

Manual review skills: Market Specialisation | Project Plan | Strategy Execution

## CFG1003 Introduction to Financial Wellbeing

Original extracted skills: Behavioural Finance | Automation Design | Management Decision Making | Debt Restructuring

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Behavioural Finance | Examine the psychological, social, cognitive and emotional factors in investment. | manual review | The course covers money decision making and investing, but it does not explicitly mention psychological or emotional factors in investment. |
| Automation Design | Manage control systems and information technology to reduce the need for human work in the production of goods and services in order to streamline operations in terms of speed, reliability and product output. | remove | The module mentions money automation, not industrial control systems or production automation. |
| Management Decision Making | Make financial decisions based on management reports. | manual review | Financial decision making is central, but the taxonomy skill is specifically about management reports in an organisational context. |
| Debt Restructuring | Assess processes to address risk of default on existing debt or evaluate opportunities to take advantage of lower available interest rates through debt restructuring. | manual review | Debt is in scope, but the description does not mention restructuring existing debt, default risk, or refinancing. |

Proposed cleaned skills: None

Manual review skills: Behavioural Finance | Management Decision Making | Debt Restructuring

## CFG1004 Financial Readiness for Young Professionals

Original extracted skills: Financial Planning | Learning Environment Design

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Financial Planning | Evaluate and develop budget in line with organisation's strategies and plans. | manual review | Financial management is a core topic, but the taxonomy description is about organisational budgeting rather than personal financial readiness. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | The blended learning format describes course delivery, not a learner capability about designing learning environments. |

Proposed cleaned skills: None

Manual review skills: Financial Planning

## CFG1500 Women's Professional Development

Original extracted skills: Learning Environment Design | Mentoring for Youths | Learning Strategy and Framework Development

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | Blended delivery is part of the course setup, but students are not taught to design learning environments. |
| Mentoring for Youths | Provide guidance to youths to facilitate their holistic development. | remove | Students receive mentoring and peer support; the description does not say they mentor youths themselves. |
| Learning Strategy and Framework Development | Design learning strategy and philosophy to define best practices for how arts students will develop the desired skills, qualities, experience, and behaviours necessary to achieve their learning objectives through the curriculum. | remove | The module supports professional development, but it does not teach students to design curriculum-level learning strategies or philosophies. |

Proposed cleaned skills: None

Manual review skills: None

## CFG1600 CommsLab Public Speaking

Original extracted skills: Practice Evaluation | Coaching and Mentoring | Client Assessment for Speech Therapy | Learner Assessments | Effective Client Communication | Learning Environment Design

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Practice Evaluation | Evaluate current and emerging psychological services and initiatives for improvements, adaptions or adoption to advance professional practice. | remove | The course is about public speaking, not evaluating psychological services or professional practice initiatives. |
| Coaching and Mentoring | Develop and implement coaching and mentoring approaches to address learner developmental needs, taking an empathetic approach to support the artistic development and expression of students. | remove | Students receive feedback and peer learning, but they are not learning to design coaching or mentoring approaches. |
| Client Assessment for Speech Therapy | Select and apply assessment methods and tools appropriate for clients and interpret findings. | remove | Public speaking practice does not involve speech-therapy assessment methods or clinical interpretation. |
| Learner Assessments | Evaluate learners' knowledge to develop self-regulated learners. | manual review | Peer learning and feedback are present, but assessing learners is not stated as a course outcome. |
| Effective Client Communication | Demonstrate effective communicative skills when communicating with clients and caregivers. | manual review | Communication is central, but the taxonomy skill is framed around client and caregiver settings rather than general presentation or pitching. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | The flipped classroom is a delivery method, not a skill students are asked to perform. |

Proposed cleaned skills: None

Manual review skills: Learner Assessments | Effective Client Communication

## CFG1600S CommsLab Public Speaking (FoS)

Original extracted skills: Practice Evaluation | Client Assessment for Speech Therapy | Learning Environment Design | Learner Assessments

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Practice Evaluation | Evaluate current and emerging psychological services and initiatives for improvements, adaptions or adoption to advance professional practice. | remove | The course is about public speaking, not evaluating psychological services or professional practice initiatives. |
| Client Assessment for Speech Therapy | Select and apply assessment methods and tools appropriate for clients and interpret findings. | remove | Public speaking practice does not involve speech-therapy assessment methods or clinical interpretation. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | The flipped classroom is a delivery method, not a skill students are asked to perform. |
| Learner Assessments | Evaluate learners' knowledge to develop self-regulated learners. | manual review | Peer learning and feedback are present, but assessing learners is not stated as a course outcome. |

Proposed cleaned skills: None

Manual review skills: Learner Assessments

## CFG2100 Introduction to Decision-Making in Business

Original extracted skills: Management Decision Making | Business Needs Analysis | Business Planning | Business Innovation | Competitive Business Strategy | Business Risk Assessment | Partnership Management | Enterprise Architecture

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Management Decision Making | Make financial decisions based on management reports. | keep | Making critical business decisions is the core stated outcome, and the simulation gives students practical decision-making experience. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business. | manual review | Students gain business insight, but the description does not explicitly cover requirements gathering, scoping, or business-case development. |
| Business Planning | Design and formulate business plans to achieve business goals. | keep | Running a commercial enterprise and applying business management strategies align with formulating plans to achieve business goals. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds. | remove | The module does not mention digitisation, ICT-led opportunities, or building new digital services. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation. | keep | The module explicitly covers business strategies in a complex competitive environment. |
| Business Risk Assessment | Articulate, communicate and assess organisational risk appetite frameworks and risk statements across the organisation. | manual review | Decision making in a simulation may involve risk, but the description does not mention organisational risk appetite frameworks or formal risk statements. |
| Partnership Management | Build cooperative partnerships with inter-organisational and external stakeholders and leverage these relations to meet organisational objectives. This includes coordination and strategising with internal and external stakeholders through close cooperation and exchange of information to solve problems. | manual review | Team development and negotiation are relevant, but the module does not explicitly cover managing inter-organisational or external partnerships. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements. | remove | The module is foundational business decision-making, not enterprise architecture, business-model evolution, or technology capability planning. |

Proposed cleaned skills: Management Decision Making | Business Planning | Competitive Business Strategy

Manual review skills: Business Needs Analysis | Business Risk Assessment | Partnership Management

## CFG3001 Career Advancement

Original extracted skills: Brand Management | Learning Environment Design

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Brand Management | Co-create the organisation's projected brand and reputation with the customer, consider customer's perspectives and the organisation's desired image and priorities. This also includes the development and execution of branding campaigns, public relations and reputation management strategies to sustain or enhance the desired brand. | manual review | Personal branding is explicit, but the taxonomy skill is written for organisational brand and reputation management with customers. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | Online delivery and live components describe the course format, not a student skill. |

Proposed cleaned skills: None

Manual review skills: Brand Management

## Aggregate Summary

- Reviewed modules: 8
- Reviewed extracted skill entries: 34
- `keep`: 3
- `manual review`: 14
- `remove`: 17

Skills most often recommended for removal:

- Learning Environment Design (5)
- Practice Evaluation (2)
- Client Assessment for Speech Therapy (2)
- Programme Delivery (1)
- Business Needs Analysis (1)
- Automation Design (1)
- Mentoring for Youths (1)
- Learning Strategy and Framework Development (1)
- Coaching and Mentoring (1)
- Business Innovation (1)
- Enterprise Architecture (1)
