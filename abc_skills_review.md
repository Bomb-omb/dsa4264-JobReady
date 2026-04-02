# Skills Review Report

Reviewed modules from `data\2025-2026_module_clean_with_prereq_skillsfuture.csv` with `10` or more extracted skills. Only exact title matches against `data\skills_taxo.csv` were evaluated.

Decision rubric:
- `keep`: directly supported by the module description
- `manual review`: somewhat plausible, but not confidently supported
- `remove`: materially off-topic or too domain-specific

## ACC2727 Business Processes, Systems and Assurance-Foundation

Original extracted skills:
```text
Auditing and Assurance Standards | Audit and Compliance | Transactional Accounting | Audit Management | Fraud Risk Management | Business Process Management | Business Process Re-engineering | Risk Assessment | Regulatory Strategy | Evidence Management | Internal Controls | Professional Standards
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Auditing and Assurance Standards | Use applicable auditing and assurance standards to carry out auditing and assurance activities | keep | The module has direct support for this skill through assurance, audit. |
| Audit and Compliance | Develop compliance processes and audit strategy for the organisation to review adherence to statutory regulatory and standards. Assessment and enhancement of the thoroughness of compliance and/or governance processes and organisation's internal controls to align with changing compliance standards. This also includes the actual conduct and/or performance of audit activities | keep | The module description directly supports this skill through audit, compliance. |
| Transactional Accounting | Apply transactional accounting to record financial events | manual review | The module suggests some coverage through transactional, but it does not fully confirm the full taxonomy definition. |
| Audit Management | Review organisational objectives, policies, procedures, structure, controls and systems to verify that the organisation's activities are efficiently managed | manual review | The module suggests some coverage through audit, but it does not fully confirm the full taxonomy definition. |
| Fraud Risk Management | Evaluate organisation's potential for occurrence of fraud and develop fraud risk awareness throughout the organisation | manual review | The module suggests some coverage through fraud, risk, but it does not fully confirm the full taxonomy definition. |
| Business Process Management | Manage and optimise an organisation's business processes for efficiency and effectiveness | keep | The module has direct support for this skill through busines, proces. |
| Business Process Re-engineering | Analyse business processes and workflows within the organisation and identification of new approaches to completely redesign business activities or optimise performance, quality and speed of services or processes including exploration of automating and streamlining processes, evaluation of associated costs and benefits of redesigning business processes, as well as identification of potential impact, change management activities and resources required | manual review | The module suggests some coverage through busines, proces, re, but it does not fully confirm the full taxonomy definition. |
| Risk Assessment | Perform assessment of risks, including fraud risks, through understanding the client's business | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Regulatory Strategy | Align regulatory activities with business strategies | keep | The module has direct support for this skill through regulatory. |
| Evidence Management | Employ forensic research methodologies to collect and manage data | manual review | The module suggests some coverage through evidence, but it does not fully confirm the full taxonomy definition. |
| Internal Controls | Evaluate effectiveness and efficiency of internal controls in the organisation | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Professional Standards | Advocate standards development to promote public confidence and build trust in society | manual review | The module suggests some coverage through professional, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Auditing and Assurance Standards`, `Audit and Compliance`, `Business Process Management`, `Risk Assessment`, `Regulatory Strategy`, `Internal Controls`

Manual review skills: `Transactional Accounting`, `Audit Management`, `Fraud Risk Management`, `Business Process Re-engineering`, `Evidence Management`, `Professional Standards`

## ACC3727 Business Processes, Systems and Assurance - Advanced

Original extracted skills:
```text
Auditing and Assurance Standards | Audit and Compliance | Quality Control and Assurance | Audit Management | Transactional Accounting | Sustainability Assurance | Systems Design | Information Technology and Network Security | Ethical Conduct and Professional Integrity | Business Process Management | IT Standards | Practitioner Inquiry | Technical Inspection | Effective Client Communication | Networking | Applications Development | Financial Acumen | Control System Programming
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Auditing and Assurance Standards | Use applicable auditing and assurance standards to carry out auditing and assurance activities | keep | The module description directly supports this skill through assurance, audit, standard. |
| Audit and Compliance | Develop compliance processes and audit strategy for the organisation to review adherence to statutory regulatory and standards. Assessment and enhancement of the thoroughness of compliance and/or governance processes and organisation's internal controls to align with changing compliance standards. This also includes the actual conduct and/or performance of audit activities | keep | The module has direct support for this skill through audit. |
| Quality Control and Assurance | Establish quality control procedures for biopharmaceutical manufacturing processes, products, equipment and systems, to ensure the desired level of compliance at all stages | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to biopharma than the module makes clear. |
| Audit Management | Review organisational objectives, policies, procedures, structure, controls and systems to verify that the organisation's activities are efficiently managed | manual review | The module suggests some coverage through audit, but it does not fully confirm the full taxonomy definition. |
| Transactional Accounting | Apply transactional accounting to record financial events | manual review | The module suggests some coverage through transactional, but it does not fully confirm the full taxonomy definition. |
| Sustainability Assurance | Evaluate and verify the accuracy, relevance, and completeness of an organisation’s sustainability reporting and information disclosure, ensuring alignment with established regulatory standards, environmental goals, social responsibilities, and economic outcomes. Enhance the transparency, credibility, and trust in an organisation’s sustainability reporting, ensuring that informed decisions can be made. | manual review | The module suggests some coverage through assurance, sustainability, but it does not fully confirm the full taxonomy definition. |
| Systems Design | Design systems to meet specified business and user requirements that are compatible with established system architectures, as well as organisational and performance standards | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Information Technology and Network Security | Manage organisation's network and data security, ensuring an ongoing rigorous review of the organisation's digital, cyber and application security and IT network infrastructures, to ensure multiple layers of defences to protect proprietary data from attack and the organisation's reputation | manual review | The module suggests some coverage through network, security, but it does not fully confirm the full taxonomy definition. |
| Ethical Conduct and Professional Integrity | Understand the professional conduct, ethics and values and comply with the relevant legislation to uphold the integrity and reputation of the profession | keep | The module has direct support for this skill through conduct, professional. |
| Business Process Management | Manage and optimise an organisation's business processes for efficiency and effectiveness | keep | The module has direct support for this skill through busines, proces. |
| IT Standards | Develop and review of standard operating procedures as well as service expectations for IT-related activities and processes. This includes the provision of clear guidelines for the organisation to carry out IT-related tasks in a manner that is effective, efficient and consistent with the IT service standards and quality standards of the organisation | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Practitioner Inquiry | Undertake systematic and data-driven investigations with other professionals to reflect, evaluate and innovate to improve their professional practice | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Technical Inspection | Execute formal inspection exercises to ensure quality, safety, and reliability adhering with technical specifications and compliance requirements | remove | The module title/description centers on `Business Processes, Systems and Assurance - Advanced` rather than `Technical Inspection` as defined in the taxonomy. |
| Effective Client Communication | Demonstrate effective communicative skills when communicating with clients and caregivers | remove | The taxonomy entry is caregiver/client communication, not audit reporting. |
| Networking | Identify and establish industry stakeholder relationships at all levels of business operations to further the organisation's strategies and objectives | keep | The module description directly supports this skill through network. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | The course discusses controls around systems development, not building applications. |
| Financial Acumen | Exercise financial insight to establish budgets for human resource (HR) activities and monitor HR operations and outcomes against financial plans | remove | The taxonomy entry is HR-budgeting specific and does not fit advanced audit and assurance. |
| Control System Programming | Develop capabilities in areas of communications and remote operations by programming logic circuits and erasable programmable read-only memory for ships, rigs and/or conversions | remove | The taxonomy description is specific to marine/offshore, which is not reflected in the module. |

Proposed cleaned skills: `Auditing and Assurance Standards`, `Audit and Compliance`, `Ethical Conduct and Professional Integrity`, `Business Process Management`, `IT Standards`, `Networking`

Manual review skills: `Quality Control and Assurance`, `Audit Management`, `Transactional Accounting`, `Sustainability Assurance`, `Systems Design`, `Information Technology and Network Security`, `Practitioner Inquiry`

## BT4012 Fraud Analytics

Original extracted skills:
```text
Monitoring and Surveillance | Artificial Intelligence Application | Threat Intelligence and Detection | Cyber Forensics | Data Visualisation | Threat Analysis and Defence | Analytics and Computational Modelling | Financial Modelling | Cyber Risk Management | Data Design
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Monitoring and Surveillance | Develop and conduct checks and observations to assess adherence to statutory regulations and standards, thoroughness of compliance controls and monitor for irregular activities. | keep | Continuous fraud monitoring is explicitly supported. |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | keep | Deep learning and explainable AI are direct module topics. |
| Threat Intelligence and Detection | Describe contemporary threats by discerning suspicious activities | keep | Threat detection is a direct module outcome. |
| Cyber Forensics | Develop and manage digital forensic investigation and reporting plan which specifies the tools, methods, procedures and practices to be used. This includes the collection, analysis and preservation of digital evidence in line with standard procedures and reporting of findings for legal proceedings | keep | Fraud and intrusion investigation directly support this skill. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | keep | The module description directly supports this skill through visualization. |
| Threat Analysis and Defence | Enable and conduct analysis of malicious threats, to examine their characteristics, behaviours, capabilities, intent and interactions with the environment as well as the development of defence and mitigation strategies and techniques to effectively combat such threats | keep | Adversarial attacks and defences are explicit topics. |
| Analytics and Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks which also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issue or requirement | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | manual review | Fraud analytics is finance-adjacent, but valuation-style financial modelling is not the main focus. |
| Cyber Risk Management | Develop cyber risk assessment and treatment techniques that can effectively pre-empt and identify significant security loopholes and weaknesses, demonstration of the business risks associated with these loopholes and provision of risk treatment and prioritisation strategies to effectively address the cyber-related risks, threats and vulnerabilities identified to ensure appropriate levels of protection, confidentiality, integrity and privacy in alignment with the security framework | keep | The module description directly supports this skill through cyber, risk. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | Data preparation fits partially, but database or data-flow design is not explicit. |

Proposed cleaned skills: `Monitoring and Surveillance`, `Artificial Intelligence Application`, `Threat Intelligence and Detection`, `Cyber Forensics`, `Data Visualisation`, `Threat Analysis and Defence`, `Cyber Risk Management`

Manual review skills: `Analytics and Computational Modelling`, `Financial Modelling`, `Data Design`

## BT4222 Mining Web Data for Business Insights

Original extracted skills:
```text
Text Analytics and Processing | Business Data Analysis | Learning Analytics | Audience Analytics | Big Data Analytics | Data Design | Customer Behaviour Analysis | Pattern Recognition Systems | Data Analysis and Interpretation | Website Design | Applications Integration
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Text Analytics and Processing | Identify, extract and analyse text data using text analytics solutions to discover themes, patterns and trends | keep | Natural language processing and text feature engineering are explicit module topics. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | keep | The module explicitly derives business insights from web data. |
| Learning Analytics | Analyse data to glean insights and drive decision making to enhance learning delivery, in accordance with governance and management policies for the handling of data at various stages of its lifecycle. | remove | The taxonomy entry is about analytics for learning delivery, which is not part of the module. |
| Audience Analytics | Perform systematic collection, analysis, and interpretation of data related to audience behaviour and engagement across various digital platforms | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | Working with web data is relevant, but database or data-model design is not explicit. |
| Customer Behaviour Analysis | Devise customer behaviour analysis tools and approaches, to perform analysis on information pertaining to customer behaviours, leading to improved customer recommendations | remove | The module title/description centers on `Mining Web Data for Business Insights` rather than `Customer Behaviour Analysis` as defined in the taxonomy. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | keep | Pattern extraction from unstructured data and machine learning are central topics. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module directly teaches extracting insights from web data. |
| Website Design | Determine and review purposes, expectations and functionalities of websites, as well as analyse the user-interface design requirements | remove | The module is about mining web data, not designing websites. |
| Applications Integration | Integrate data or functions from one application program with that of another application program - involves development of an integration plan, programming and the identification and utilisation of appropriate middleware to optimise the connectivity and performance of disparate applications across target environments | manual review | APIs are mentioned, but the middleware/integration scope is broader than the module description. |

Proposed cleaned skills: `Text Analytics and Processing`, `Business Data Analysis`, `Pattern Recognition Systems`, `Data Analysis and Interpretation`

Manual review skills: `Audience Analytics`, `Big Data Analytics`, `Data Design`, `Applications Integration`

## CLC2202 Research Methods for Community Development

Original extracted skills:
```text
Research Design | Community Development | Data Collection and Analysis | Research | Research Findings Communication | Business Data Analysis | Quantitative Research | Arts Education Research | Data Design | Project After Action Review
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Community Development | Build, grow and manage community relationships across a variety of online and offline platforms to generate brand awareness, understand customers' needs, increase customer engagement and develop customer loyalty | manual review | The module title fits, but the taxonomy definition is closer to community marketing than social/community development practice. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | keep | The module description directly supports this skill through analysi, collection. |
| Research | Optimising manufacturing processes, material developments and development of new product line | remove | The taxonomy description is manufacturing/new-product R&D, not social-science research methods. |
| Research Findings Communication | Communicate research findings effectively to the target audiences using communication methods in accordance to established standards in the scientific community | keep | The module explicitly includes dissemination of research results. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | Data analysis is supported, but business-intelligence framing is not explicit. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | keep | Quantitative research methods are explicitly supported. |
| Arts Education Research | Investigate a research focus and hypothesis leading to the generation of insights on current developments, trends and innovative methods of learning delivery and programme design. | remove | The module is about community-development research methods, not arts-education research. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | remove | Database or data-model design is not part of the module description. |
| Project After Action Review | Set and determine project after action review (AAR) as well as review and evaluate success of strategic plan after action plans have been implemented | manual review | Programme and process evaluation make this plausible, but after-action review is not explicitly named. |

Proposed cleaned skills: `Research Design`, `Data Collection and Analysis`, `Research Findings Communication`, `Quantitative Research`

Manual review skills: `Community Development`, `Business Data Analysis`, `Project After Action Review`

## CN3101A Chemical Engineering Process Lab

Original extracted skills:
```text
Process Engineering Design | Process Control | Chemical Processing | Heat Treatment Process | Laboratory Data Analysis | Waste Recycling and Recovery Management | Technical Inspection | Failure Analysis | Process Validation | Data Design
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Process Engineering Design | Apply process design principles, engineering standards, control and safety strategies for the development of new and existing process plants | keep | The module has direct support for this skill through engineer, proces. |
| Process Control | Apply process control to monitor and optimise process plant performance and quality of production output | keep | The module description directly supports this skill through control, proces. |
| Chemical Processing | Perform chemical processing applications on parts and components using appropriate tools, equipment, materials and methods in accordance with applicable technical manuals and organisational procedures | keep | The module description directly supports this skill through chemical. |
| Heat Treatment Process | Analyse effects of heat treatments to determine suitable materials and treatment processes to achieve required material properties for manufactured components and products | remove | The lab covers heat transfer, not metallurgical heat-treatment processes. |
| Laboratory Data Analysis | Analyse laboratory data | keep | The module description directly supports this skill through analysi, laboratory. |
| Waste Recycling and Recovery Management | Assess the potential of an organisation’s waste streams for reduce, reuse and/or recycle. Identify, evaluate and recommend opportunities for the development and integration of new sustainable technologies and waste recovery methodologies that convert waste materials into valuable resources. Establish and implement well-integrated waste recovery systems within organisations, aligning with national and global environmental standards, and organisational sustainability goals. | remove | The module title/description centers on `Chemical Engineering Process Lab` rather than `Waste Recycling and Recovery Management` as defined in the taxonomy. |
| Technical Inspection | Execute formal inspection exercises to ensure quality, safety, and reliability adhering with technical specifications and compliance requirements | manual review | The module suggests some coverage through technical, but it does not fully confirm the full taxonomy definition. |
| Failure Analysis | Examine the electrical and physical defects evidence to verify the causes of failure as well as identify the failure modes | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Process Validation | Verify that processes are reproducible and consistent in delivering quality products according to specifications, and in line with international regulations | manual review | The module suggests some coverage through proces, validation, but it does not fully confirm the full taxonomy definition. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Process Engineering Design`, `Process Control`, `Chemical Processing`, `Laboratory Data Analysis`

Manual review skills: `Technical Inspection`, `Failure Analysis`, `Process Validation`, `Data Design`

## CN4102 Chemical Engineering Lab

Original extracted skills:
```text
Process Engineering Design | Process Control | Chemical Processing | Laboratory Data Analysis | Heat Treatment Process | Waste Recycling and Recovery Management | Technical Inspection | Failure Analysis | Process Validation | Data Design
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Process Engineering Design | Apply process design principles, engineering standards, control and safety strategies for the development of new and existing process plants | keep | The module has direct support for this skill through engineer, proces. |
| Process Control | Apply process control to monitor and optimise process plant performance and quality of production output | keep | The module description directly supports this skill through control, proces. |
| Chemical Processing | Perform chemical processing applications on parts and components using appropriate tools, equipment, materials and methods in accordance with applicable technical manuals and organisational procedures | keep | The module description directly supports this skill through chemical. |
| Laboratory Data Analysis | Analyse laboratory data | keep | The module description directly supports this skill through analysi, laboratory. |
| Heat Treatment Process | Analyse effects of heat treatments to determine suitable materials and treatment processes to achieve required material properties for manufactured components and products | manual review | The module suggests some coverage through heat, proces, but it does not fully confirm the full taxonomy definition. |
| Waste Recycling and Recovery Management | Assess the potential of an organisation’s waste streams for reduce, reuse and/or recycle. Identify, evaluate and recommend opportunities for the development and integration of new sustainable technologies and waste recovery methodologies that convert waste materials into valuable resources. Establish and implement well-integrated waste recovery systems within organisations, aligning with national and global environmental standards, and organisational sustainability goals. | remove | The module title/description centers on `Chemical Engineering Lab` rather than `Waste Recycling and Recovery Management` as defined in the taxonomy. |
| Technical Inspection | Execute formal inspection exercises to ensure quality, safety, and reliability adhering with technical specifications and compliance requirements | manual review | The module suggests some coverage through technical, but it does not fully confirm the full taxonomy definition. |
| Failure Analysis | Examine the electrical and physical defects evidence to verify the causes of failure as well as identify the failure modes | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Process Validation | Verify that processes are reproducible and consistent in delivering quality products according to specifications, and in line with international regulations | manual review | The module suggests some coverage through proces, validation, but it does not fully confirm the full taxonomy definition. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Process Engineering Design`, `Process Control`, `Chemical Processing`, `Laboratory Data Analysis`

Manual review skills: `Heat Treatment Process`, `Technical Inspection`, `Failure Analysis`, `Process Validation`, `Data Design`

## CN4245R Data Based Process Characterisation

Original extracted skills:
```text
Data Design | Process Modelling | Process Monitoring | Data Engineering | Data-Mining and Modelling | Data and Statistical Analytics | Process Optimisation | Laboratory Data Analysis | Control System Programming | Data Collection and Preparation | Systems Integration | New Product Introduction
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Process Modelling | Model manufacturing processes in order to ensure successful implementation | keep | Process modelling is explicitly named and central to the course. |
| Process Monitoring | Verify that routine manufacturing processes are consistently within a state of control | manual review | The module suggests some coverage through monitor, proces, but it does not fully confirm the full taxonomy definition. |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data-Mining and Modelling | Establish and deploy data modelling techniques to support narrative and predictive analytics efforts and identify trends and patterns for simulation and forecasting purposes | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Process Optimisation | Analyse biopharmaceuticals manufacturing processes and identify adjustments that will reduce costs of manufacturing and increase quality, throughput and efficiency | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to biopharma than the module makes clear. |
| Laboratory Data Analysis | Analyse laboratory data | keep | The module has direct support for this skill through analysi. |
| Control System Programming | Develop capabilities in areas of communications and remote operations by programming logic circuits and erasable programmable read-only memory for ships, rigs and/or conversions | remove | The module covers process control and system identification, not ship/rig control-circuit programming. |
| Data Collection and Preparation | Collect human resource (HR) data from employees for the purpose of generating business and HR insights | remove | The matched taxonomy entry is HR-employee-data focused and unrelated here. |
| Systems Integration | Realise the system-of-interest by progressively combining system elements in accordance with design requirements and the integration strategy | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| New Product Introduction | Support new production by validating build plan to achieve cost-effective production and assembly as well as meeting design specifications | manual review | The module suggests some coverage through product, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Process Modelling`, `Laboratory Data Analysis`

Manual review skills: `Data Design`, `Process Monitoring`, `Data Engineering`, `Data-Mining and Modelling`, `Data and Statistical Analytics`, `Process Optimisation`, `Systems Integration`, `New Product Introduction`

## CP3100 Information Systems and Analytics Research Methodology

Original extracted skills:
```text
Research Design | Data Collection and Analysis | Research Findings Communication | Analytics and Computational Modelling | Arts Education Research | Research Proposal Development | Ethical Conduct and Professional Integrity | Systems Architecture | Laboratory Data Analysis | Interviewing | Applications Development | Quality Improvement and Safe Practices
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | keep | Research design is explicitly named in the module. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | keep | Data collection and analysis are explicit module topics. |
| Research Findings Communication | Communicate research findings effectively to the target audiences using communication methods in accordance to established standards in the scientific community | keep | The module supports communication of research outcomes. |
| Analytics and Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks which also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issue or requirement | manual review | Quantitative methods are present, but advanced computational modelling is not explicit. |
| Arts Education Research | Investigate a research focus and hypothesis leading to the generation of insights on current developments, trends and innovative methods of learning delivery and programme design. | remove | The taxonomy entry is about arts education, not IS/analytics research methods. |
| Research Proposal Development | Develop research questions, proposals and study protocols | keep | Proposal development is directly supported. |
| Ethical Conduct and Professional Integrity | Understand the professional conduct, ethics and values and comply with the relevant legislation to uphold the integrity and reputation of the profession | keep | Research ethics and professional conduct are directly relevant. |
| Systems Architecture | Design and implement the underlying systems that drive games and underpin gameplay experience | remove | The taxonomy entry is about game systems, not research methodology. |
| Laboratory Data Analysis | Analyse laboratory data | remove | The module is not lab-based. |
| Interviewing | Conduct and follow up on interviews according to established interview objectives and organisation's selection procedures | keep | In-depth interviews are explicitly covered. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | There is no software-build scope in the module. |
| Quality Improvement and Safe Practices | Drive continuous improvement, risk management and implementation of safety design principles to achieve quality and patient safety outcomes | remove | The taxonomy entry is healthcare-specific and unsupported. |

Proposed cleaned skills: `Research Design`, `Data Collection and Analysis`, `Research Findings Communication`, `Research Proposal Development`, `Ethical Conduct and Professional Integrity`, `Interviewing`

Manual review skills: `Analytics and Computational Modelling`

## CS1010 Programming Methodology

Original extracted skills:
```text
Programming and Coding | Computational Design | Control System Programming | Software Design | Applications Development | Programme Evaluation | Problem Identification | Data Design | Test Planning | Pattern Recognition Systems
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Programming and Coding | Produce the technology required for a visual effects (VFX) project | manual review | Programming is explicit, but the taxonomy definition is VFX-specific. |
| Computational Design | Use programming and computational strategies for design processes to enable design optioneering, automation and optimisation | keep | The module description directly supports this skill through computational. |
| Control System Programming | Develop capabilities in areas of communications and remote operations by programming logic circuits and erasable programmable read-only memory for ships, rigs and/or conversions | remove | The taxonomy entry is about marine control hardware, not introductory programming. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | Coding and debugging are covered, but the full application lifecycle is broader than this module. |
| Programme Evaluation | Evaluate the effectiveness and efficiency of programmes, and contribute to continuous programme improvement | remove | The module title/description centers on `Programming Methodology` rather than `Programme Evaluation` as defined in the taxonomy. |
| Problem Identification | Classify problems and associated implications as well as provide recommendations to resolve issues at hand | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Test Planning | Develop testing plans and procedures by determining scope and risks, identifying the objects of testing, selecting test methods and tools, and controlling test implementation | manual review | The module suggests some coverage through test, but it does not fully confirm the full taxonomy definition. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | remove | The module is about introductory programming, not pattern-recognition systems. |

Proposed cleaned skills: `Computational Design`

Manual review skills: `Programming and Coding`, `Software Design`, `Applications Development`, `Problem Identification`, `Data Design`, `Test Planning`

## CS1010E Programming Methodology

Original extracted skills:
```text
Programming and Coding | Computational Design | Control System Programming | Software Design | Applications Development | Programme Evaluation | Problem Identification | Data Design | Test Planning | Pattern Recognition Systems
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Programming and Coding | Produce the technology required for a visual effects (VFX) project | manual review | Programming is explicit, but the taxonomy definition is VFX-specific. |
| Computational Design | Use programming and computational strategies for design processes to enable design optioneering, automation and optimisation | keep | The module description directly supports this skill through computational. |
| Control System Programming | Develop capabilities in areas of communications and remote operations by programming logic circuits and erasable programmable read-only memory for ships, rigs and/or conversions | remove | The taxonomy entry is about marine control hardware, not introductory programming. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | Coding and debugging are covered, but the full application lifecycle is broader than this module. |
| Programme Evaluation | Evaluate the effectiveness and efficiency of programmes, and contribute to continuous programme improvement | remove | The module title/description centers on `Programming Methodology` rather than `Programme Evaluation` as defined in the taxonomy. |
| Problem Identification | Classify problems and associated implications as well as provide recommendations to resolve issues at hand | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Test Planning | Develop testing plans and procedures by determining scope and risks, identifying the objects of testing, selecting test methods and tools, and controlling test implementation | manual review | The module suggests some coverage through test, but it does not fully confirm the full taxonomy definition. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | remove | The module is about introductory programming, not pattern-recognition systems. |

Proposed cleaned skills: `Computational Design`

Manual review skills: `Programming and Coding`, `Software Design`, `Applications Development`, `Problem Identification`, `Data Design`, `Test Planning`

## CS1010J Programming Methodology

Original extracted skills:
```text
Programming and Coding | Computational Design | Control System Programming | Software Design | Applications Development | Programme Evaluation | Problem Identification | Data Design | Test Planning | Pattern Recognition Systems
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Programming and Coding | Produce the technology required for a visual effects (VFX) project | manual review | Programming is explicit, but the taxonomy definition is VFX-specific. |
| Computational Design | Use programming and computational strategies for design processes to enable design optioneering, automation and optimisation | keep | The module description directly supports this skill through computational. |
| Control System Programming | Develop capabilities in areas of communications and remote operations by programming logic circuits and erasable programmable read-only memory for ships, rigs and/or conversions | remove | The taxonomy entry is about marine control hardware, not introductory programming. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | Coding and debugging are covered, but the full application lifecycle is broader than this module. |
| Programme Evaluation | Evaluate the effectiveness and efficiency of programmes, and contribute to continuous programme improvement | remove | The module title/description centers on `Programming Methodology` rather than `Programme Evaluation` as defined in the taxonomy. |
| Problem Identification | Classify problems and associated implications as well as provide recommendations to resolve issues at hand | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Test Planning | Develop testing plans and procedures by determining scope and risks, identifying the objects of testing, selecting test methods and tools, and controlling test implementation | manual review | The module suggests some coverage through test, but it does not fully confirm the full taxonomy definition. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | remove | The module is about introductory programming, not pattern-recognition systems. |

Proposed cleaned skills: `Computational Design`

Manual review skills: `Programming and Coding`, `Software Design`, `Applications Development`, `Problem Identification`, `Data Design`, `Test Planning`

## CS2106 Introduction to Operating Systems

Original extracted skills:
```text
Systems Architecture | System Architecture Design | Process Integration | Systems Design | Digital Asset and File Management | Process Modelling | Scheduling and Slot Coordination | Embedded System Integration | Architecture Design | Operation Management | Process Validation | Security Architecture | Interface Management | Software Configuration | Resource Management | IT Standards
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Systems Architecture | Design and implement the underlying systems that drive games and underpin gameplay experience | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to games/VFX/media than the module makes clear. |
| System Architecture Design | Synthesise system architecture baselines for ships, rigs, conversions and/or automated production lines to satisfy stakeholder requirements | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to marine/offshore than the module makes clear. |
| Process Integration | Integrate process loops and/or architecture to optimise process interactions between and within process modules as well as formulate strategies for yield performance improvements | manual review | The module suggests some coverage through proces, but it does not fully confirm the full taxonomy definition. |
| Systems Design | Design systems to meet specified business and user requirements that are compatible with established system architectures, as well as organisational and performance standards | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Digital Asset and File Management | Develop and implement systematic procedures to organise digital content in collaborative and networked environments | manual review | File systems fit partially, but the taxonomy is framed around collaborative digital-content management. |
| Process Modelling | Model manufacturing processes in order to ensure successful implementation | keep | The module description directly supports this skill through proces. |
| Scheduling and Slot Coordination | Develop and manage airline schedules and slots by applying optimisation techniques | remove | The module covers OS scheduling, but the taxonomy entry is airline-slot specific. |
| Embedded System Integration | Implement control systems to perform pre-defined tasks and also real-time monitoring for the real world | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Architecture Design | Utilise holistic design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The module suggests some coverage through architecture, but it does not fully confirm the full taxonomy definition. |
| Operation Management | Manage organisation's operational effectiveness and efficiency in accordance with regulatory frameworks and requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Process Validation | Verify that processes are reproducible and consistent in delivering quality products according to specifications, and in line with international regulations | manual review | The module suggests some coverage through proces, but it does not fully confirm the full taxonomy definition. |
| Security Architecture | Design security architectures and controls; either embedding of security principles into the design of architectures to mitigate the risks posed by new technologies and business practices, or the actual design and specification of implementable security components, along with the accompanying control measures, to meet defined business security needs | keep | OS protection mechanisms and user authentication are explicit module topics. |
| Interface Management | Perform interface management activities to integrate systems on ships, rigs and/or conversions | remove | The taxonomy description is marine/offshore specific, not operating systems. |
| Software Configuration | Configure software products, analytics and modelling solutions, and apply and/or modify scripts and automation tools to integrate and deploy releases to various platforms and operating environments | remove | The module title/description centers on `Introduction to Operating Systems` rather than `Software Configuration` as defined in the taxonomy. |
| Resource Management | Plan and manage resources to ensure optimisation of resources and sustainability of business operations | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| IT Standards | Develop and review of standard operating procedures as well as service expectations for IT-related activities and processes. This includes the provision of clear guidelines for the organisation to carry out IT-related tasks in a manner that is effective, efficient and consistent with the IT service standards and quality standards of the organisation | remove | The module title/description centers on `Introduction to Operating Systems` rather than `IT Standards` as defined in the taxonomy. |

Proposed cleaned skills: `Process Modelling`, `Security Architecture`

Manual review skills: `Systems Architecture`, `System Architecture Design`, `Process Integration`, `Systems Design`, `Digital Asset and File Management`, `Embedded System Integration`, `Architecture Design`, `Operation Management`, `Process Validation`, `Resource Management`

## CS3203 Software Engineering Project

Original extracted skills:
```text
Software Design | Applications Development | Systems Integration | Systems Design | Software Configuration | Group Work Evaluation | Test Planning | Quality Standards | Design Writing | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | keep | Software analysis, design, implementation, and testing are direct module topics. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Systems Integration | Realise the system-of-interest by progressively combining system elements in accordance with design requirements and the integration strategy | keep | System integration is directly supported by the software engineering project context. |
| Systems Design | Design systems to meet specified business and user requirements that are compatible with established system architectures, as well as organisational and performance standards | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Software Configuration | Configure software products, analytics and modelling solutions, and apply and/or modify scripts and automation tools to integrate and deploy releases to various platforms and operating environments | manual review | The module suggests some coverage through software, but it does not fully confirm the full taxonomy definition. |
| Group Work Evaluation | Evaluate group work processes and specialised intervention strategies for quality and effectiveness of outcomes | manual review | The module suggests some coverage through evaluation, group, but it does not fully confirm the full taxonomy definition. |
| Test Planning | Develop testing plans and procedures by determining scope and risks, identifying the objects of testing, selecting test methods and tools, and controlling test implementation | manual review | The module suggests some coverage through test, but it does not fully confirm the full taxonomy definition. |
| Quality Standards | Develop, review and communicate a clear, quality expectations and standards within an organisation that are aligned to the company's values and business objectives. This encompasses the setting and implementation of quality expectations for IT products and services delivered to both internal or external clients | remove | The module title/description centers on `Software Engineering Project` rather than `Quality Standards` as defined in the taxonomy. |
| Design Writing | Convey a design story, idea or concept in a compelling and engaging manner through writing | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | remove | The module is about software engineering, not financial analysis. |

Proposed cleaned skills: `Software Design`, `Systems Integration`

Manual review skills: `Applications Development`, `Systems Design`, `Software Configuration`, `Group Work Evaluation`, `Test Planning`, `Design Writing`

## CS3221 Operating Systems Design and Pragmatics

Original extracted skills:
```text
Systems Architecture | System Architecture Design | Applications Development | Process Integration | Embedded Systems Interface Design | Scheduling and Slot Coordination | IT Standards | Process Monitoring | Software Configuration | Technology Scanning | Digital Asset and File Management
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Systems Architecture | Design and implement the underlying systems that drive games and underpin gameplay experience | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to games/VFX/media than the module makes clear. |
| System Architecture Design | Synthesise system architecture baselines for ships, rigs, conversions and/or automated production lines to satisfy stakeholder requirements | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to marine/offshore than the module makes clear. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Process Integration | Integrate process loops and/or architecture to optimise process interactions between and within process modules as well as formulate strategies for yield performance improvements | manual review | The module suggests some coverage through proces, but it does not fully confirm the full taxonomy definition. |
| Embedded Systems Interface Design | Design and set up interface and interconnections from or among sensors, through a network, to a main location, to enable transmission of information | manual review | The module suggests some coverage through interface, but it does not fully confirm the full taxonomy definition. |
| Scheduling and Slot Coordination | Develop and manage airline schedules and slots by applying optimisation techniques | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to aviation than the module makes clear. |
| IT Standards | Develop and review of standard operating procedures as well as service expectations for IT-related activities and processes. This includes the provision of clear guidelines for the organisation to carry out IT-related tasks in a manner that is effective, efficient and consistent with the IT service standards and quality standards of the organisation | remove | The module title/description centers on `Operating Systems Design and Pragmatics` rather than `IT Standards` as defined in the taxonomy. |
| Process Monitoring | Verify that routine manufacturing processes are consistently within a state of control | manual review | The module suggests some coverage through proces, but it does not fully confirm the full taxonomy definition. |
| Software Configuration | Configure software products, analytics and modelling solutions, and apply and/or modify scripts and automation tools to integrate and deploy releases to various platforms and operating environments | remove | The module title/description centers on `Operating Systems Design and Pragmatics` rather than `Software Configuration` as defined in the taxonomy. |
| Technology Scanning | Evaluate the digital technology environment and the impact of digital technology development | remove | The module title/description centers on `Operating Systems Design and Pragmatics` rather than `Technology Scanning` as defined in the taxonomy. |
| Digital Asset and File Management | Develop and implement systematic procedures to organise digital content in collaborative and networked environments | manual review | The module suggests some coverage through file, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: None

Manual review skills: `Systems Architecture`, `System Architecture Design`, `Applications Development`, `Process Integration`, `Embedded Systems Interface Design`, `Scheduling and Slot Coordination`, `Process Monitoring`, `Digital Asset and File Management`

## CS3223 Database Systems Implementation

Original extracted skills:
```text
Database Administration | Transactional Accounting | Data Engineering | Data Design | Access Control Management | Applications Integration | Process Analytical Technology Implementation | Process Optimisation | Process Control | Inventory Management
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Database Administration | Perform Installation, coordination and upgrading of databases and database servers, performance monitoring and troubleshooting. This includes monitoring user access to database and optimisation of database performance, planning for backup and recovery, archived data maintenance and reporting | keep | Storage, query processing, concurrency, and recovery directly support database administration. |
| Transactional Accounting | Apply transactional accounting to record financial events | remove | The module covers database transactions, not accounting. |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | keep | Database implementation and storage/retrieval concerns directly support data design. |
| Access Control Management | Manage access control to ensure authorised access in accordance with the organisation's policies | manual review | Multi-user databases make this plausible, but policy-oriented access management is not explicit. |
| Applications Integration | Integrate data or functions from one application program with that of another application program - involves development of an integration plan, programming and the identification and utilisation of appropriate middleware to optimise the connectivity and performance of disparate applications across target environments | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Process Analytical Technology Implementation | Apply Process Analytical Technology to design, analyse and control manufacturing processes to enhance production efficiency and quality | remove | The taxonomy entry is manufacturing-specific and unsupported. |
| Process Optimisation | Analyse biopharmaceuticals manufacturing processes and identify adjustments that will reduce costs of manufacturing and increase quality, throughput and efficiency | remove | The taxonomy entry is biopharma-specific rather than database-focused. |
| Process Control | Apply process control to monitor and optimise process plant performance and quality of production output | keep | The module description directly supports this skill through control, proces. |
| Inventory Management | formulate and implement inventory management strategies targeted at ensuring availability of equipment, tools and materials for engineering projects for the purpose of construction, operations and maintenance works | remove | The module is about database systems, not inventory management. |

Proposed cleaned skills: `Database Administration`, `Data Design`, `Process Control`

Manual review skills: `Data Engineering`, `Access Control Management`, `Applications Integration`

## CS3242 3D Modeling and Animation

Original extracted skills:
```text
3D Modelling | 2D Animation | Digital and Interactive Design | Character Design | Computational Modelling | Render Management | Scriptwriting | Lighting Operations | Learning Environment Design | Physics Concepts Application
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| 3D Modelling | Generate 3D models using a variety of modelling software to represent characteristics of a real-world system | keep | The module description directly supports this skill through 3d. |
| 2D Animation | Create 2D animated sequences for incorporation into animated films, videos, games or other media content | manual review | The module suggests some coverage through animation, but it does not fully confirm the full taxonomy definition. |
| Digital and Interactive Design | Design and execute digital innovation technologies such as virtual and augmented realities, advanced digital projected and 360-degree photography and videography to create interactive experiences for audiences. This includes 3D projection mapping, holographic projection, AR / VR and other related technologies | manual review | The module suggests some coverage through digital, but it does not fully confirm the full taxonomy definition. |
| Character Design | Design and develop characters to meet the creative and technical requirements of production | manual review | The module suggests some coverage through character, but it does not fully confirm the full taxonomy definition. |
| Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks. This also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issues or requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Render Management | Render 3D models, scenes, or visual effects into 2D images or sequences, which can be viewed as final output | keep | The module has direct support for this skill through render. |
| Scriptwriting | Create compelling and engaging scripts for media content of different formats on various platforms | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Lighting Operations | Manage the set-up and operations of lighting equipment during productions | manual review | The module suggests some coverage through light, but it does not fully confirm the full taxonomy definition. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | The module title/description centers on `3D Modeling and Animation` rather than `Learning Environment Design` as defined in the taxonomy. |
| Physics Concepts Application | Apply physics concepts to solve engineering problems | manual review | The module suggests some coverage through concept, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `3D Modelling`, `Render Management`

Manual review skills: `2D Animation`, `Digital and Interactive Design`, `Character Design`, `Computational Modelling`, `Scriptwriting`, `Lighting Operations`, `Physics Concepts Application`

## CS4224 Distributed Databases

Original extracted skills:
```text
Common Data Environment Management | Data Strategy | Database Administration | Data Design | Cloud Computing Application | Infrastructure Deployment | Systems Integration | Content Delivery Network Operations | Automated Distribution Management | Transactional Accounting
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Common Data Environment Management | Implement Common Data Environment (CDE) to improve the management of data and information to facilitate decision making and increase the efficiency of project delivery | remove | The taxonomy entry is construction/project-delivery oriented. |
| Data Strategy | Develop a robust and coherent data strategy and support architectures, policies, practices and procedures that enable the organisation to manage and utilise data in an effective manner. This includes introduction of innovative ways of organising, managing and integrating the data of the organisation to ensure their viability and ability to drive business value. It also includes the setting of information storage, sharing, handling and usage protocols to support alignment with relevant legislation and business strategies | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Database Administration | Perform Installation, coordination and upgrading of databases and database servers, performance monitoring and troubleshooting. This includes monitoring user access to database and optimisation of database performance, planning for backup and recovery, archived data maintenance and reporting | keep | Distributed query processing, transactions, and replication directly support this skill. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | keep | Distributed database design and data management directly support this skill. |
| Cloud Computing Application | Implement cloud solutions to enhance business performance and security of IT systems | manual review | Cloud appears as context, but the module is not mainly a cloud-solutions course. |
| Infrastructure Deployment | Set up, deploy and decommission infrastructure components and associated equipment in accordance with a set plan and established safety and/or quality procedures. This includes the assessment and preparation of appropriate site locations, infrastructure, the development of an installation plan, layout at the site, the testing of on-site systems, infrastructure components, equipment and the correction of issues and/or malfunctions | remove | The module title/description centers on `Distributed Databases` rather than `Infrastructure Deployment` as defined in the taxonomy. |
| Systems Integration | Realise the system-of-interest by progressively combining system elements in accordance with design requirements and the integration strategy | keep | The module description directly supports this skill through integration. |
| Content Delivery Network Operations | Manage and content delivery over digital platforms by designing, deploying, operating and maintaining Content Delivery Networks (CDNs) | remove | The module title/description centers on `Distributed Databases` rather than `Content Delivery Network Operations` as defined in the taxonomy. |
| Automated Distribution Management | Maintain, oversee and review automated processes and systems within a department | remove | The taxonomy entry is about operational distribution processes, not distributed databases. |
| Transactional Accounting | Apply transactional accounting to record financial events | remove | The module covers database transactions, not accounting. |

Proposed cleaned skills: `Database Administration`, `Data Design`, `Systems Integration`

Manual review skills: `Data Strategy`, `Cloud Computing Application`

## CS4350 Game Development Project

Original extracted skills:
```text
Gameplay Development | Game Level Development | Game Engine Development | Design Creation and Development | Strategy Execution | Motion Graphics | Interface Management | 3D Animation | Artificial Intelligence Application | Networking
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Gameplay Development | Develop programs for the implementation of gameplay functionalities and features for games | keep | Gameplay development is directly aligned with the module. |
| Game Level Development | Develop scripts to implement quests, missions and challenges to achieve the vision of gameplay | keep | Game-level work is directly aligned with the module. |
| Game Engine Development | Design and develop a suite of customisable tools and programs for specific aspects of game development including graphics, physics, artificial intelligence, gameplay, level and sound development modules, which form the basis of game development | keep | Core technical game-development work directly supports this skill. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Strategy Execution | Develop and implement plans to achieve organisational and departmental strategies and goals | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Motion Graphics | Execute creation of motion graphics for content | manual review | The module suggests some coverage through graphic, but it does not fully confirm the full taxonomy definition. |
| Interface Management | Perform interface management activities to integrate systems on ships, rigs and/or conversions | remove | The taxonomy description is marine/offshore specific. |
| 3D Animation | Create 3D animated sequences depicting motion through computer-based visual graphics for use in films, games or other media content | keep | 3D graphics and animation align directly with the module. |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | remove | The module title/description centers on `Game Development Project` rather than `Artificial Intelligence Application` as defined in the taxonomy. |
| Networking | Identify and establish industry stakeholder relationships at all levels of business operations to further the organisation's strategies and objectives | remove | The taxonomy entry is about stakeholder networking, not technical game-development work. |

Proposed cleaned skills: `Gameplay Development`, `Game Level Development`, `Game Engine Development`, `3D Animation`

Manual review skills: `Design Creation and Development`, `Strategy Execution`, `Motion Graphics`

## DAO2703 Operations and Technology Management

Original extracted skills:
```text
Sustainability Management | Operation Management | Lean Manufacturing | Sustainability Assurance | Manufacturing Technology | Enterprise Architecture | Quality System Management | Service Planning and Implementation | Advanced Processing Technology | Robotic and Automation Technology Application | IT Standards | Artificial Intelligence Application
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Sustainability Management | Plan, develop and roll out of an organisation-wide sustainability strategy. This includes the assessment of the organisation's utilisation and/or consumption of energy and other resources, vis-a-vis the availability and stability of supply sources and external best practices and standards in sustainability. This also includes the on-going monitoring and tracking of energy and/or resource-consumption over time, to identify impact on the organisation's internal and external environment as well as potential improvements in energy- or resource-efficiency. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Operation Management | Manage organisation's operational effectiveness and efficiency in accordance with regulatory frameworks and requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Lean Manufacturing | Apply concepts, tools and techniques of "lean" to improve efficiency in the workplace | manual review | The module suggests some coverage through lean, manufactur, but it does not fully confirm the full taxonomy definition. |
| Sustainability Assurance | Evaluate and verify the accuracy, relevance, and completeness of an organisation’s sustainability reporting and information disclosure, ensuring alignment with established regulatory standards, environmental goals, social responsibilities, and economic outcomes. Enhance the transparency, credibility, and trust in an organisation’s sustainability reporting, ensuring that informed decisions can be made. | remove | The module title/description centers on `Operations and Technology Management` rather than `Sustainability Assurance` as defined in the taxonomy. |
| Manufacturing Technology | Optimise manufacturing processes, utilising available and applicable technologies | keep | The module description directly supports this skill through manufactur. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | manual review | The module suggests some coverage through enterprise, but it does not fully confirm the full taxonomy definition. |
| Quality System Management | Coordinate and direct the organisation's activities to meet customer and regulatory requirements as well as identify opportunities for improvement. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Service Planning and Implementation | Develop and implement strategies and plans for the service operations | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Advanced Processing Technology | Design and apply advanced processing technology to manufacture food products that are appealing, tasty, nutritious and have a long shelf life | manual review | The module suggests some coverage through advanc, but it does not fully confirm the full taxonomy definition. |
| Robotic and Automation Technology Application | Integrate automation technologies and robotic systems to enhance precision and productivity and reduce reliance on manual tasks | manual review | The module suggests some coverage through robotic, but it does not fully confirm the full taxonomy definition. |
| IT Standards | Develop and review of standard operating procedures as well as service expectations for IT-related activities and processes. This includes the provision of clear guidelines for the organisation to carry out IT-related tasks in a manner that is effective, efficient and consistent with the IT service standards and quality standards of the organisation | remove | The module title/description centers on `Operations and Technology Management` rather than `IT Standards` as defined in the taxonomy. |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | remove | The module title/description centers on `Operations and Technology Management` rather than `Artificial Intelligence Application` as defined in the taxonomy. |

Proposed cleaned skills: `Manufacturing Technology`

Manual review skills: `Sustainability Management`, `Operation Management`, `Lean Manufacturing`, `Enterprise Architecture`, `Quality System Management`, `Service Planning and Implementation`, `Advanced Processing Technology`, `Robotic and Automation Technology Application`

## DAO2703A Operations and Technology Management

Original extracted skills:
```text
Sustainability Management | Operation Management | Lean Manufacturing | Sustainability Assurance | Manufacturing Technology | Enterprise Architecture | Quality System Management | Service Planning and Implementation | Advanced Processing Technology | Robotic and Automation Technology Application | IT Standards | Artificial Intelligence Application
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Sustainability Management | Plan, develop and roll out of an organisation-wide sustainability strategy. This includes the assessment of the organisation's utilisation and/or consumption of energy and other resources, vis-a-vis the availability and stability of supply sources and external best practices and standards in sustainability. This also includes the on-going monitoring and tracking of energy and/or resource-consumption over time, to identify impact on the organisation's internal and external environment as well as potential improvements in energy- or resource-efficiency. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Operation Management | Manage organisation's operational effectiveness and efficiency in accordance with regulatory frameworks and requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Lean Manufacturing | Apply concepts, tools and techniques of "lean" to improve efficiency in the workplace | manual review | The module suggests some coverage through lean, manufactur, but it does not fully confirm the full taxonomy definition. |
| Sustainability Assurance | Evaluate and verify the accuracy, relevance, and completeness of an organisation’s sustainability reporting and information disclosure, ensuring alignment with established regulatory standards, environmental goals, social responsibilities, and economic outcomes. Enhance the transparency, credibility, and trust in an organisation’s sustainability reporting, ensuring that informed decisions can be made. | remove | The module title/description centers on `Operations and Technology Management` rather than `Sustainability Assurance` as defined in the taxonomy. |
| Manufacturing Technology | Optimise manufacturing processes, utilising available and applicable technologies | keep | The module description directly supports this skill through manufactur. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | manual review | The module suggests some coverage through enterprise, but it does not fully confirm the full taxonomy definition. |
| Quality System Management | Coordinate and direct the organisation's activities to meet customer and regulatory requirements as well as identify opportunities for improvement. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Service Planning and Implementation | Develop and implement strategies and plans for the service operations | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Advanced Processing Technology | Design and apply advanced processing technology to manufacture food products that are appealing, tasty, nutritious and have a long shelf life | manual review | The module suggests some coverage through advanc, but it does not fully confirm the full taxonomy definition. |
| Robotic and Automation Technology Application | Integrate automation technologies and robotic systems to enhance precision and productivity and reduce reliance on manual tasks | manual review | The module suggests some coverage through robotic, but it does not fully confirm the full taxonomy definition. |
| IT Standards | Develop and review of standard operating procedures as well as service expectations for IT-related activities and processes. This includes the provision of clear guidelines for the organisation to carry out IT-related tasks in a manner that is effective, efficient and consistent with the IT service standards and quality standards of the organisation | remove | The module title/description centers on `Operations and Technology Management` rather than `IT Standards` as defined in the taxonomy. |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | remove | The module title/description centers on `Operations and Technology Management` rather than `Artificial Intelligence Application` as defined in the taxonomy. |

Proposed cleaned skills: `Manufacturing Technology`

Manual review skills: `Sustainability Management`, `Operation Management`, `Lean Manufacturing`, `Enterprise Architecture`, `Quality System Management`, `Service Planning and Implementation`, `Advanced Processing Technology`, `Robotic and Automation Technology Application`

## DBA3803 Predictive Analytics in Business

Original extracted skills:
```text
Business Data Analysis | Pattern Recognition Systems | Data-Mining and Modelling | Data Visualisation | Generative AI Model Selection | Tree Assessments | Big Data Analytics | Financial Modelling | Business Excellence | Analytics and Computational Modelling
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | keep | The module has direct support for this skill through busines. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data-Mining and Modelling | Establish and deploy data modelling techniques to support narrative and predictive analytics efforts and identify trends and patterns for simulation and forecasting purposes | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Generative AI Model Selection | Choose the most appropriate model for the development of a generative AI system for a use case, from a variety of external models, and based on published metrics and user experiments. | remove | The module covers predictive analytics, not generative AI model choice. |
| Tree Assessments | Conduct comprehensive tree assessments to support decision making pertaining to development of new landscapes, maintenance of existing landscape sites, safety and tree conservation | remove | The taxonomy entry is about landscape tree conservation, not predictive analytics. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Excellence | Develop and implement policies and processes to achieve business excellence | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Analytics and Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks which also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issue or requirement | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Business Data Analysis`

Manual review skills: `Pattern Recognition Systems`, `Data-Mining and Modelling`, `Data Visualisation`, `Big Data Analytics`, `Financial Modelling`, `Business Excellence`, `Analytics and Computational Modelling`

## DOS4716 Advanced Operations and Supply Chain Management

Original extracted skills:
```text
Cost Management | Continuous Quality Improvement | Sustainability Management | Risk Management | Process Modelling | Business Process Re-engineering | Enterprise Architecture | Engineering Problem Solving | Applications Development | Lean Manufacturing | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Cost Management | Analyse, plan and manage costs for cost efficiency and expense reduction | keep | The module description directly supports this skill through cost. |
| Continuous Quality Improvement | Implement on-going efforts to improve products, services, and/or processes through leveraging on opportunities to streamline work, increase quality and reduce waste | manual review | The module suggests some coverage through continuou, improvement, but it does not fully confirm the full taxonomy definition. |
| Sustainability Management | Plan, develop and roll out of an organisation-wide sustainability strategy. This includes the assessment of the organisation's utilisation and/or consumption of energy and other resources, vis-a-vis the availability and stability of supply sources and external best practices and standards in sustainability. This also includes the on-going monitoring and tracking of energy and/or resource-consumption over time, to identify impact on the organisation's internal and external environment as well as potential improvements in energy- or resource-efficiency. | keep | The module description directly supports this skill through sustainability. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | manual review | The module suggests some coverage through risk, but it does not fully confirm the full taxonomy definition. |
| Process Modelling | Model manufacturing processes in order to ensure successful implementation | manual review | The module suggests some coverage through proces, but it does not fully confirm the full taxonomy definition. |
| Business Process Re-engineering | Analyse business processes and workflows within the organisation and identification of new approaches to completely redesign business activities or optimise performance, quality and speed of services or processes including exploration of automating and streamlining processes, evaluation of associated costs and benefits of redesigning business processes, as well as identification of potential impact, change management activities and resources required | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Engineering Problem Solving | Apply the eight disciplines methodology for systematic problem solving including root cause analysis, failure mode effect and analysis, containment actions, and corrective actions and preventive actions in accordance with organisational systems and processes | manual review | The module suggests some coverage through engineer, solv, but it does not fully confirm the full taxonomy definition. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Lean Manufacturing | Apply concepts, tools and techniques of "lean" to improve efficiency in the workplace | keep | Lean and continuous improvement are explicit syllabus topics. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Cost Management`, `Sustainability Management`, `Business Process Re-engineering`, `Lean Manufacturing`

Manual review skills: `Continuous Quality Improvement`, `Risk Management`, `Process Modelling`, `Enterprise Architecture`, `Engineering Problem Solving`, `Applications Development`, `Financial Analysis`

## DOS4811 Data Visualisation

Original extracted skills:
```text
Infographics and Data Visualisation | Data Storytelling and Visualisation | Data Strategy | Supply Chain Management | Data Collection and Management | Data Analysis and Interpretation | Financial Analysis | Data Collection and Analysis | Visual Communication | Interaction Design Practice | Learning Experience Evaluation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Infographics and Data Visualisation | Present data using meaningful visual illustrations, iconographies, graphs and charts for easy and accessible discovery and communication of data insights aimed at specific business objectives | manual review | The module suggests some coverage through visualization, but it does not fully confirm the full taxonomy definition. |
| Data Storytelling and Visualisation | Combine data insights, dynamic visual displays with illustrative and interactive graphics and narrative representative formats to present patterns, trends, meaning, messages and analytical insights from data or new concepts in a strategic manner | manual review | The module suggests some coverage through visualization, but it does not fully confirm the full taxonomy definition. |
| Data Strategy | Develop a robust and coherent data strategy and support architectures, policies, practices and procedures that enable the organisation to manage and utilise data in an effective manner. This includes introduction of innovative ways of organising, managing and integrating the data of the organisation to ensure their viability and ability to drive business value. It also includes the setting of information storage, sharing, handling and usage protocols to support alignment with relevant legislation and business strategies | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Supply Chain Management | Develop and maintain supply chain processes, comprising feedstock, production, storage, and export, to ensure supply and demand are managed in an integrated manner and in full alignment with production availability, downtime, plant turnarounds and market conditions | manual review | The module suggests some coverage through chain, supply, but it does not fully confirm the full taxonomy definition. |
| Data Collection and Management | Employ sound research methodologies to collect and manage data | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module has direct support for this skill through analysi. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Visual Communication | Design visual communication outputs to elicit emotional connections and responses from target audiences | manual review | The module suggests some coverage through visual, but it does not fully confirm the full taxonomy definition. |
| Interaction Design Practice | Develop digital and/or physical interactions across technology, products, space and services media to enhance relationships and engagement with users | remove | The module title/description centers on `Data Visualisation` rather than `Interaction Design Practice` as defined in the taxonomy. |
| Learning Experience Evaluation | Assess overall learning experiences to measure effectiveness and drive excellence across all learning activities | remove | The module title/description centers on `Data Visualisation` rather than `Learning Experience Evaluation` as defined in the taxonomy. |

Proposed cleaned skills: `Data Analysis and Interpretation`

Manual review skills: `Infographics and Data Visualisation`, `Data Storytelling and Visualisation`, `Data Strategy`, `Supply Chain Management`, `Data Collection and Management`, `Financial Analysis`, `Data Collection and Analysis`, `Visual Communication`

## DSA2101 Essential Data Analytics Tools: Data Visualisation

Original extracted skills:
```text
Data Visualisation | Data and Information Visualisation | Data and Statistical Analytics | Data Design | Data Storytelling and Visualisation | Business Data Analysis | Big Data Analytics | Data Cleaning and Retargeting | Data Strategy | Information Gathering and Analysis | Data Migration
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | keep | Data visualisation is the direct focus of the module. |
| Data and Information Visualisation | Combine communication, data science and design to present complex insights and information in a manner that facilitates meaningful storytelling and better decision-making for the organisation | keep | The module directly focuses on data visualisation. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | keep | The module supports extracting and communicating insights from data. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Storytelling and Visualisation | Combine data insights, dynamic visual displays with illustrative and interactive graphics and narrative representative formats to present patterns, trends, meaning, messages and analytical insights from data or new concepts in a strategic manner | keep | Storytelling with data is directly supported by the module. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | keep | The module has direct support for this skill through analysi. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | Analytics is central, but big-data scale is not stated explicitly. |
| Data Cleaning and Retargeting | Clean and retarget motion capture data onto character rigs, ensuring accurate and realistic movements | remove | The taxonomy entry is about motion-capture/character-rigging work. |
| Data Strategy | Develop a robust and coherent data strategy and support architectures, policies, practices and procedures that enable the organisation to manage and utilise data in an effective manner. This includes introduction of innovative ways of organising, managing and integrating the data of the organisation to ensure their viability and ability to drive business value. It also includes the setting of information storage, sharing, handling and usage protocols to support alignment with relevant legislation and business strategies | remove | Enterprise data governance and strategy are not part of the module. |
| Information Gathering and Analysis | Collect and analyse information and data to obtain business insights for business activities | keep | Turning raw data into useful information is a direct module outcome. |
| Data Migration | Plan and perform activities to migrate data between computer storage types or file formats | remove | The module does not cover data migration. |

Proposed cleaned skills: `Data Visualisation`, `Data and Information Visualisation`, `Data and Statistical Analytics`, `Data Storytelling and Visualisation`, `Business Data Analysis`, `Information Gathering and Analysis`

Manual review skills: `Data Design`, `Big Data Analytics`

## DSA2361 Data Analytics for Customer Insights

Original extracted skills:
```text
Market Research and Analysis | Business Data Analysis | Customer Acquisition Management | Big Data Analytics | Customer Management | Data-Mining and Modelling | Customer Loyalty | Quantitative Research | Trading Analysis | Customer Service Delivery | Financial Modelling
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Market Research and Analysis | Develop market analysis frameworks and objectives to guide and conduct analyses of market trends, developments, competitive factors and economic changes to identify useful business insights, drive economic decisions and forecast market needs | keep | Customer profiling, segmentation, and marketing strategy directly support this skill. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | keep | The module applies analytics to customer and marketing decisions. |
| Customer Acquisition Management | Develop customer acquisition strategies as well as foster customer relationships to attract new customers | manual review | The module is more explicit about retention and customer value than acquisition. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Customer Management | Manage customers with the goal of improving business relationships with customers and achieving service requirements | manual review | The skill is plausible, but operational customer-management duties are not explicit. |
| Data-Mining and Modelling | Establish and deploy data modelling techniques to support narrative and predictive analytics efforts and identify trends and patterns for simulation and forecasting purposes | keep | Predictive customer analytics directly support this skill. |
| Customer Loyalty | Develop and manage customer loyalty and retention programmes to foster long-term relationships with customers | keep | Retention, upsell, and CLV align directly with customer-loyalty work. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | keep | The module uses quantitative analysis to understand customer behaviour. |
| Trading Analysis | Develop market research reports to support trading strategies | remove | The module is about customer analytics, not trading. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | remove | The module uses customer metrics, not valuation-oriented financial modelling. |

Proposed cleaned skills: `Market Research and Analysis`, `Business Data Analysis`, `Data-Mining and Modelling`, `Customer Loyalty`, `Quantitative Research`

Manual review skills: `Customer Acquisition Management`, `Big Data Analytics`, `Customer Management`

## DSC3225 Project Management

Original extracted skills:
```text
Project Management | Project Risk Management | Project Coordination | Project Integration | Change Management | Product Management | Project Quality | Organisation Management | Programme Management | Construction Technology | Engineering Problem Solving | Applications Development
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Project Management | Execute projects by managing stakeholder engagement, resources, budgets and resolving problems | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Project Risk Management | Manage risks relating to specific projects as precaution against internal and external vulnerabilities | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Project Coordination | Coordinate project activities and workflows in collaboration with project teams and relevant stakeholders, as determined by project plans, to fulfil expected project outcomes and objectives | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Project Integration | Set programme direction as well as balance overall project management functions across the project life cycle | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Change Management | Manage changes and developments within teams and organisation | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | manual review | The module suggests some coverage through product, but it does not fully confirm the full taxonomy definition. |
| Project Quality | Manage project processes and deliverables, according to stakeholder requirements and objectives, to improve customer satisfaction levels | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Organisation Management | Oversee and manage centre operations to drive operational excellence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Programme Management | Manage multiple projects within the organisation to identify efficiencies of common policies, procedures and practices | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Construction Technology | Identify and apply the most suitable and effective construction processes and technologies to achieve project objectives | keep | The module has direct support for this skill through construction. |
| Engineering Problem Solving | Apply the eight disciplines methodology for systematic problem solving including root cause analysis, failure mode effect and analysis, containment actions, and corrective actions and preventive actions in accordance with organisational systems and processes | remove | The module title/description centers on `Project Management` rather than `Engineering Problem Solving` as defined in the taxonomy. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Project Management`, `Project Risk Management`, `Change Management`, `Construction Technology`

Manual review skills: `Project Coordination`, `Project Integration`, `Product Management`, `Project Quality`, `Organisation Management`, `Programme Management`, `Applications Development`

## DSC4213 Analytical Tools for Consulting

Original extracted skills:
```text
Supply Chain Management | Risk Management | Risk Assessment | Data-Mining and Modelling | Computational Modelling | Customer Acquisition Management | Consumer Intelligence Analysis | Cash Flow Management | Enterprise Architecture | Order Fulfilment Administration | Benchmarking | Trend Forecasting | Analytical Method Validation | Process Optimisation | Applications Development | Problem Management | Supplier Sourcing
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Supply Chain Management | Develop and maintain supply chain processes, comprising feedstock, production, storage, and export, to ensure supply and demand are managed in an integrated manner and in full alignment with production availability, downtime, plant turnarounds and market conditions | keep | The module description directly supports this skill through chain, supply. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | Decision and risk analysis are explicit module topics. |
| Risk Assessment | Perform assessment of risks, including fraud risks, through understanding the client's business | manual review | The module suggests some coverage through risk, but it does not fully confirm the full taxonomy definition. |
| Data-Mining and Modelling | Establish and deploy data modelling techniques to support narrative and predictive analytics efforts and identify trends and patterns for simulation and forecasting purposes | keep | Data mining, simulation, and optimization are core analytical topics. |
| Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks. This also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issues or requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Customer Acquisition Management | Develop customer acquisition strategies as well as foster customer relationships to attract new customers | manual review | The module suggests some coverage through customer, but it does not fully confirm the full taxonomy definition. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | manual review | CRM and customer-segmentation cases support it somewhat, but the taxonomy definition is broader. |
| Cash Flow Management | Manage and maintain business units' cash flow by consolidating data and performing analysis on cash inflow and outflow | keep | The module description directly supports this skill through cash, flow. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Order Fulfilment Administration | Administer receiving, processing, delivery and optimisation processes for orders in order to support business and customer requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Benchmarking | Compare organisational performance to other organisations and industries | keep | Benchmarking is explicitly named in the module description. |
| Trend Forecasting | Drive the practice of collecting and comparing information over time to identify trends and patterns, in order to predict and plan for future events | keep | Forecasting is explicitly named in the module description. |
| Analytical Method Validation | Verify analytical methods used to ensure accuracy, validity and reliability of methods | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Process Optimisation | Analyse biopharmaceuticals manufacturing processes and identify adjustments that will reduce costs of manufacturing and increase quality, throughput and efficiency | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to biopharma than the module makes clear. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | The module uses analytical software but does not teach application development. |
| Problem Management | Manage the lifecycle of problems to prevent problems and incidents from occurring, eliminate recurring incidents and minimise impact of unavoidable incidents | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Supplier Sourcing | Formulate organisational strategies to source for, manage and review supplier contracts | remove | Supplier sourcing is not a central learning outcome of the module. |

Proposed cleaned skills: `Supply Chain Management`, `Risk Management`, `Data-Mining and Modelling`, `Cash Flow Management`, `Benchmarking`, `Trend Forecasting`

Manual review skills: `Risk Assessment`, `Computational Modelling`, `Customer Acquisition Management`, `Consumer Intelligence Analysis`, `Enterprise Architecture`, `Order Fulfilment Administration`, `Analytical Method Validation`, `Process Optimisation`, `Problem Management`

## DSC4214 Co-ordination and Flexibility in SCM

Original extracted skills:
```text
Supply Chain Management | Operation Management | Production Operations | Market Research and Analysis | Mathematical Concepts Application | Management Decision Making | Analytics and Computational Modelling | Risk Management | Problem Management | Applications Development
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Supply Chain Management | Develop and maintain supply chain processes, comprising feedstock, production, storage, and export, to ensure supply and demand are managed in an integrated manner and in full alignment with production availability, downtime, plant turnarounds and market conditions | manual review | The module suggests some coverage through chain, supply, but it does not fully confirm the full taxonomy definition. |
| Operation Management | Manage organisation's operational effectiveness and efficiency in accordance with regulatory frameworks and requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Production Operations | Manage the coordination and execution of production operations | keep | The module description directly supports this skill through production. |
| Market Research and Analysis | Develop market analysis frameworks and objectives to guide and conduct analyses of market trends, developments, competitive factors and economic changes to identify useful business insights, drive economic decisions and forecast market needs | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Mathematical Concepts Application | Apply mathematical concepts to solve engineering problems | keep | The module has direct support for this skill through concept. |
| Management Decision Making | Make financial decisions based on management reports | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Analytics and Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks which also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issue or requirement | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Problem Management | Manage the lifecycle of problems to prevent problems and incidents from occurring, eliminate recurring incidents and minimise impact of unavoidable incidents | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Production Operations`, `Mathematical Concepts Application`

Manual review skills: `Supply Chain Management`, `Operation Management`, `Market Research and Analysis`, `Management Decision Making`, `Analytics and Computational Modelling`, `Risk Management`, `Problem Management`, `Applications Development`

## DSC4215 Data Visualisation

Original extracted skills:
```text
Infographics and Data Visualisation | Data Storytelling and Visualisation | Data Strategy | Supply Chain Management | Data Collection and Management | Data Analysis and Interpretation | Financial Analysis | Data Collection and Analysis | Visual Communication | Interaction Design Practice | Learning Experience Evaluation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Infographics and Data Visualisation | Present data using meaningful visual illustrations, iconographies, graphs and charts for easy and accessible discovery and communication of data insights aimed at specific business objectives | keep | The module directly teaches visual communication of data. |
| Data Storytelling and Visualisation | Combine data insights, dynamic visual displays with illustrative and interactive graphics and narrative representative formats to present patterns, trends, meaning, messages and analytical insights from data or new concepts in a strategic manner | keep | The module explicitly supports storytelling with data. |
| Data Strategy | Develop a robust and coherent data strategy and support architectures, policies, practices and procedures that enable the organisation to manage and utilise data in an effective manner. This includes introduction of innovative ways of organising, managing and integrating the data of the organisation to ensure their viability and ability to drive business value. It also includes the setting of information storage, sharing, handling and usage protocols to support alignment with relevant legislation and business strategies | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Supply Chain Management | Develop and maintain supply chain processes, comprising feedstock, production, storage, and export, to ensure supply and demand are managed in an integrated manner and in full alignment with production availability, downtime, plant turnarounds and market conditions | manual review | Supply-chain examples may appear, but the module itself is about visualisation. |
| Data Collection and Management | Employ sound research methodologies to collect and manage data | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | Interpreting data and communicating it visually are direct module outcomes. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | remove | The module is about visualisation rather than financial analysis. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | keep | Collecting and analyzing data is part of the visualisation workflow. |
| Visual Communication | Design visual communication outputs to elicit emotional connections and responses from target audiences | keep | Visual communication is a direct module outcome. |
| Interaction Design Practice | Develop digital and/or physical interactions across technology, products, space and services media to enhance relationships and engagement with users | remove | The module title/description centers on `Data Visualisation` rather than `Interaction Design Practice` as defined in the taxonomy. |
| Learning Experience Evaluation | Assess overall learning experiences to measure effectiveness and drive excellence across all learning activities | remove | The taxonomy entry is education-specific and unsupported. |

Proposed cleaned skills: `Infographics and Data Visualisation`, `Data Storytelling and Visualisation`, `Data Analysis and Interpretation`, `Data Collection and Analysis`, `Visual Communication`

Manual review skills: `Data Strategy`, `Supply Chain Management`, `Data Collection and Management`

## DSE1101 Introductory Data Science for Economics

Original extracted skills:
```text
Data and Statistical Analytics | Business Data Analysis | Data Engineering | Data Design | Financial Analysis | Big Data Analytics | Learning Analytics | Macroeconomic Analysis | Data Collection and Management | Social Policy Evaluation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | keep | The module description directly supports this skill through analysi, finance. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | keep | The module description directly supports this skill through big. |
| Learning Analytics | Analyse data to glean insights and drive decision making to enhance learning delivery, in accordance with governance and management policies for the handling of data at various stages of its lifecycle. | keep | The module description directly supports this skill through learn. |
| Macroeconomic Analysis | Evaluate impact of external factors on the organisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Data Collection and Management | Employ sound research methodologies to collect and manage data | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Social Policy Evaluation | Evaluate existing social policies to determine currency, relevance and alignment to national priorities and social needs | remove | The module title/description centers on `Introductory Data Science for Economics` rather than `Social Policy Evaluation` as defined in the taxonomy. |

Proposed cleaned skills: `Financial Analysis`, `Big Data Analytics`, `Learning Analytics`

Manual review skills: `Data and Statistical Analytics`, `Business Data Analysis`, `Data Engineering`, `Data Design`, `Macroeconomic Analysis`, `Data Collection and Management`

## DSE4212 Data Science in FinTech

Original extracted skills:
```text
Financial Modelling | Financial Analysis | Derivatives Trading Management | Risk Management | Data Engineering | Portfolio Management | Business Data Analysis | Data and Statistical Analytics | Analytics and Computational Modelling | Financial Transactions | Data Visualisation | Big Data Analytics
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | keep | The module description directly supports this skill through finance. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | keep | The module description directly supports this skill through analysi, finance. |
| Derivatives Trading Management | Perform structured trades for proprietary and risk management objectives by identifying market-making opportunities | keep | The module has direct support for this skill through derivativ. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Portfolio Management | Manage systematically the IT investments, projects, services and activities within a company, in line with business objectives and priorities. This involves the development of a framework to evaluate potential costs and benefits and make key decisions about IT investments, internal allocation and utilisation of IT resources and/or assets and any changes to IT processes or services offered | manual review | The module suggests some coverage through portfolio, but it does not fully confirm the full taxonomy definition. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The module suggests some coverage through statistical, but it does not fully confirm the full taxonomy definition. |
| Analytics and Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks which also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issue or requirement | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Financial Modelling`, `Financial Analysis`, `Derivatives Trading Management`, `Risk Management`

Manual review skills: `Data Engineering`, `Portfolio Management`, `Business Data Analysis`, `Data and Statistical Analytics`, `Analytics and Computational Modelling`, `Financial Transactions`, `Data Visualisation`, `Big Data Analytics`

## EE4802 Learning from Data

Original extracted skills:
```text
Data Engineering | Engineering Problem Solving | Data and Statistical Analytics | Big Data Analytics | Business Data Analysis | Data Design | Data Visualisation | Quality Engineering | Pattern Recognition Systems | Data Sharing
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The module suggests some coverage through engineer, but it does not fully confirm the full taxonomy definition. |
| Engineering Problem Solving | Apply the eight disciplines methodology for systematic problem solving including root cause analysis, failure mode effect and analysis, containment actions, and corrective actions and preventive actions in accordance with organisational systems and processes | manual review | The module suggests some coverage through engineer, problem, solv, but it does not fully confirm the full taxonomy definition. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Quality Engineering | Create, deploy and maintain quality-related systems, processes and tools to establish an environment that supports process and product quality | manual review | The module suggests some coverage through engineer, but it does not fully confirm the full taxonomy definition. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Sharing | Assess the value of data to achieve a competitive advantage and business objectives | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: None

Manual review skills: `Data Engineering`, `Engineering Problem Solving`, `Data and Statistical Analytics`, `Big Data Analytics`, `Business Data Analysis`, `Data Design`, `Data Visualisation`, `Quality Engineering`, `Pattern Recognition Systems`, `Data Sharing`

## EG4301 Innovation & Design Capstone

Original extracted skills:
```text
Solutions Design Thinking | Problem Management | Applications Development | Solutioning | Digital Techniques Application | Problem Identification | Organisational Impact Analysis | Apply teamwork in the workplace | Proposal Management | Strategy Planning
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Solutions Design Thinking | Construct solution based upon logic, imagination, intuition, and systemic reasoning, to explore possibilities of what can be and create desired outcomes that benefit the organisation and customers | remove | The taxonomy description is specific to construction/BIM, which is not reflected in the module. |
| Problem Management | Manage the lifecycle of problems to prevent problems and incidents from occurring, eliminate recurring incidents and minimise impact of unavoidable incidents | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Solutioning | Generate solutions by systematic analysis of the problem, proposing preventive and/or corrective measures and evaluating the effectiveness of the measures from different perspectives | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Digital Techniques Application | Apply and use principles of digital techniques and electronic instrument systems for maintenance, repair, overhaul or manufacturing of aircraft systems | remove | The taxonomy description is specific to aviation, which is not reflected in the module. |
| Problem Identification | Classify problems and associated implications as well as provide recommendations to resolve issues at hand | manual review | The module suggests some coverage through problem, but it does not fully confirm the full taxonomy definition. |
| Organisational Impact Analysis | Assess the impact of learning solutions and interventions on organisation's desired outcomes and identify ways to enhance learning effectiveness | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Apply teamwork in the workplace | Work as a team and participate in team activities in their work area | remove | The module title/description centers on `Innovation & Design Capstone` rather than `Apply teamwork in the workplace` as defined in the taxonomy. |
| Proposal Management | Research, strategise and draft business proposals to respond to business opportunities | remove | The module title/description centers on `Innovation & Design Capstone` rather than `Proposal Management` as defined in the taxonomy. |
| Strategy Planning | Develop organisational strategies and policies by analysing the impact of internal and external influencing factors and seeking consultation from relevant stakeholders. | remove | The module title/description centers on `Innovation & Design Capstone` rather than `Strategy Planning` as defined in the taxonomy. |

Proposed cleaned skills: None

Manual review skills: `Problem Management`, `Applications Development`, `Solutioning`, `Problem Identification`, `Organisational Impact Analysis`

## ESE4407 Environmental Forensics

Original extracted skills:
```text
Environmental Protection Management | Hazardous Substances Management | Risk Assessment | Environment Impact Assessment | Environment Observation | Ecology in Landscapes | Computational Modelling | Cyber Forensics | Regulatory Compliances in Water Supply Network Environment Management | Regulatory Strategy
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Environmental Protection Management | Establish policies and procedures for sustainable environment practices covering green procurement, gas emissions, disposal methods, product quality standards and regulatory compliance | manual review | The module suggests some coverage through environmental, protection, but it does not fully confirm the full taxonomy definition. |
| Hazardous Substances Management | Manage the handling of hazardous materials during collection, transportation, storage and disposal processes including spillage incidents | manual review | The module suggests some coverage through substanc, but it does not fully confirm the full taxonomy definition. |
| Risk Assessment | Perform assessment of risks, including fraud risks, through understanding the client's business | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Environment Impact Assessment | Evaluate and analyse the potential environmental and social consequences of proposed projects, policies, or developments, incorporating regulatory standards, environmental and social science approaches, and stakeholder insights. Inform decision-making by providing information on potential risks, as well as recommendations for minimising ecological and social impacts and promoting sustainable development. | manual review | The module suggests some coverage through assessment, environment, but it does not fully confirm the full taxonomy definition. |
| Environment Observation | Measure situations by discerning the environment | manual review | The module suggests some coverage through environment, but it does not fully confirm the full taxonomy definition. |
| Ecology in Landscapes | Adopt principles of ecology in the design, implementation and management of landscapes | keep | The module has direct support for this skill through ecology. |
| Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks. This also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issues or requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Cyber Forensics | Develop and manage digital forensic investigation and reporting plan which specifies the tools, methods, procedures and practices to be used. This includes the collection, analysis and preservation of digital evidence in line with standard procedures and reporting of findings for legal proceedings | manual review | The module suggests some coverage through forensic, but it does not fully confirm the full taxonomy definition. |
| Regulatory Compliances in Water Supply Network Environment Management | Preparation, Manage regulatory compliance in Water Supply Network environment to protect water supply integrity sampling and analysing of water samples to safeguard raw water quality in reservoirs and waterways | manual review | The module suggests some coverage through environment, regulatory, but it does not fully confirm the full taxonomy definition. |
| Regulatory Strategy | Align regulatory activities with business strategies | manual review | The module suggests some coverage through regulatory, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Risk Assessment`, `Ecology in Landscapes`

Manual review skills: `Environmental Protection Management`, `Hazardous Substances Management`, `Environment Impact Assessment`, `Environment Observation`, `Computational Modelling`, `Cyber Forensics`, `Regulatory Compliances in Water Supply Network Environment Management`, `Regulatory Strategy`

## FIN2704 Finance

Original extracted skills:
```text
Financial Statements Analysis | Capital Management | Financial Transactions | Business Needs Analysis | Financial Budgeting | Financial Planning | Risk Management | Management Decision Making | Project Plan | Valuation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Financial Statements Analysis | Analyse financial statements in accordance with the applicable frameworks | keep | The module description directly supports this skill through analysi, finance, statement. |
| Capital Management | Calculate capital adequacy ratios to determine capital buffers necessary for the bank or financial institution, while optimising returns on capital based on capital allocation strategies | manual review | Capital structure and allocation are relevant, but the taxonomy definition is about bank capital adequacy. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | remove | The course is about core finance concepts rather than business-requirements analysis. |
| Financial Budgeting | Prepare organisational budgets to support short- and long-term business plans through forecasting, allocation and financial policy settings | keep | The module description directly supports this skill through budget, finance. |
| Financial Planning | Evaluate and develop budget in line with organisation's strategies and plans | keep | Financial planning is explicitly covered in the module. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | Risk and return analysis directly support this skill. |
| Management Decision Making | Make financial decisions based on management reports | keep | The module explicitly builds financial decision-making capability. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | remove | Capital budgeting and financial planning do not make this a project-planning module. |
| Valuation | Perform valuation for business and financial assets for deal structuring | keep | Stock and bond valuation are explicit topics in the module. |

Proposed cleaned skills: `Financial Statements Analysis`, `Financial Budgeting`, `Financial Planning`, `Risk Management`, `Management Decision Making`, `Valuation`

Manual review skills: `Capital Management`, `Financial Transactions`

## FIN2704X Finance

Original extracted skills:
```text
Financial Statements Analysis | Capital Management | Financial Transactions | Business Needs Analysis | Financial Budgeting | Financial Planning | Risk Management | Management Decision Making | Project Plan | Valuation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Financial Statements Analysis | Analyse financial statements in accordance with the applicable frameworks | keep | The module description directly supports this skill through analysi, finance, statement. |
| Capital Management | Calculate capital adequacy ratios to determine capital buffers necessary for the bank or financial institution, while optimising returns on capital based on capital allocation strategies | manual review | Capital structure and allocation are relevant, but the taxonomy definition is about bank capital adequacy. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | remove | The course is about core finance concepts rather than business-requirements analysis. |
| Financial Budgeting | Prepare organisational budgets to support short- and long-term business plans through forecasting, allocation and financial policy settings | keep | The module description directly supports this skill through budget, finance. |
| Financial Planning | Evaluate and develop budget in line with organisation's strategies and plans | keep | Financial planning is explicitly covered in the module. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | Risk and return analysis directly support this skill. |
| Management Decision Making | Make financial decisions based on management reports | keep | The module explicitly builds financial decision-making capability. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | remove | Capital budgeting and financial planning do not make this a project-planning module. |
| Valuation | Perform valuation for business and financial assets for deal structuring | keep | Stock and bond valuation are explicit topics in the module. |

Proposed cleaned skills: `Financial Statements Analysis`, `Financial Budgeting`, `Financial Planning`, `Risk Management`, `Management Decision Making`, `Valuation`

Manual review skills: `Capital Management`, `Financial Transactions`

## FIN4713 Advanced Portfolio Management: Securities Analysis & Valuation

Original extracted skills:
```text
Value Analysis | Portfolio Management | Valuation | Financial Transactions | Research | Financial Modelling | Trading Management | Business Needs Analysis | Cash Flow Reporting | Qualitative Analysis | Laboratory Management
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Value Analysis | Establish the organisational value stream, enhance value-add and reduce costs | remove | The module is about security valuation, not value-stream analysis. |
| Portfolio Management | Manage systematically the IT investments, projects, services and activities within a company, in line with business objectives and priorities. This involves the development of a framework to evaluate potential costs and benefits and make key decisions about IT investments, internal allocation and utilisation of IT resources and/or assets and any changes to IT processes or services offered | manual review | The module suggests some coverage through portfolio, but it does not fully confirm the full taxonomy definition. |
| Valuation | Perform valuation for business and financial assets for deal structuring | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Research | Optimising manufacturing processes, material developments and development of new product line | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | keep | The module description directly supports this skill through finance. |
| Trading Management | Perform trades and take positions in various products in accordance with trading plans | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Cash Flow Reporting | Maintain business units' cash flow reports by consolidating data and performing analysis on cash inflow and outflow | keep | The module description directly supports this skill through cash, flow, report. |
| Qualitative Analysis | Formulate research questions and hypotheses, identify qualitative data sources for analysis of securities and provide investment recommendations based on analysis | keep | The module has direct support for this skill through analysi. |
| Laboratory Management | Implement Good Laboratory Practice procedures to ensure that performance, quality, health, and safety standards are met | remove | Hands-on finance lab projects are not laboratory operations. |

Proposed cleaned skills: `Valuation`, `Financial Modelling`, `Cash Flow Reporting`, `Qualitative Analysis`

Manual review skills: `Portfolio Management`, `Financial Transactions`, `Research`, `Trading Management`, `Business Needs Analysis`

## ID2322 Materials and Production

Original extracted skills:
```text
Manufacturing Technology | Material Studies and Production Processes | Concept Creation for Production Design | Production Design | Production Operations | Materials Inspection | Design for Additive Manufacturing | Materials Qualification | Production Technical Services | Lighting Operations | Furniture and Furnishing Maintenance
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Manufacturing Technology | Optimise manufacturing processes, utilising available and applicable technologies | keep | The module description directly supports this skill through manufactur. |
| Material Studies and Production Processes | Administer the study of material properties and applications to facilitate production, construction, engineering and processing of materials into specific designs | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to construction/BIM than the module makes clear. |
| Concept Creation for Production Design | Develop the initial concepts or ideas for creation of designs | keep | The module description directly supports this skill through concept, production. |
| Production Design | Research, conceptualise and execute the creative vision of productions | keep | The module description directly supports this skill through production. |
| Production Operations | Manage the coordination and execution of production operations | keep | The module description directly supports this skill through production. |
| Materials Inspection | Verify correctness and usability of vendor products and services through specification matching and quality checks | manual review | The module suggests some coverage through material, but it does not fully confirm the full taxonomy definition. |
| Design for Additive Manufacturing | Create optimised designs specifically tailored for additive manufacturing processes with the understanding of the capabilities and limitations of various additive manufacturing processes and integrate materials, machine capabilities and design considerations to achieve desired functionality. | keep | The module has direct support for this skill through manufactur. |
| Materials Qualification | Manage the quality of materials to ensure material specifications conform to product requirements | keep | The module has direct support for this skill through material. |
| Production Technical Services | Operate technical services in the production environment | manual review | The module suggests some coverage through production, but it does not fully confirm the full taxonomy definition. |
| Lighting Operations | Manage the set-up and operations of lighting equipment during productions | remove | Materials and production here refer to manufacturing, not lighting equipment operations. |
| Furniture and Furnishing Maintenance | Maintain the cleanliness and hygiene of furniture and furnishing in a safe manner | manual review | The module suggests some coverage through furniture, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Manufacturing Technology`, `Concept Creation for Production Design`, `Production Design`, `Production Operations`, `Design for Additive Manufacturing`, `Materials Qualification`

Manual review skills: `Material Studies and Production Processes`, `Materials Inspection`, `Production Technical Services`, `Furniture and Furnishing Maintenance`

## ID4121 Project Research

Original extracted skills:
```text
Design Creation and Development | Research Design | Design Writing | Market Research | Product Management | Project Management | Business Opportunities Development | Applications Development | Trends Evaluation and Application | Documentation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Design Writing | Convey a design story, idea or concept in a compelling and engaging manner through writing | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module description directly supports this skill through market. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | manual review | The module suggests some coverage through product, but it does not fully confirm the full taxonomy definition. |
| Project Management | Execute projects by managing stakeholder engagement, resources, budgets and resolving problems | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Opportunities Development | Develop and implement plans to enhance organisation's business performance and growth | manual review | The module suggests some coverage through opportunity, but it does not fully confirm the full taxonomy definition. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Trends Evaluation and Application | Keep abreast of current developments and trends, and apply domain knowledge to trends within the social sector | manual review | The module suggests some coverage through evaluation, but it does not fully confirm the full taxonomy definition. |
| Documentation | Write clear, concise and readable reports supported by facts and evidence | manual review | The module suggests some coverage through documentation, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Market Research`

Manual review skills: `Design Creation and Development`, `Research Design`, `Design Writing`, `Product Management`, `Project Management`, `Business Opportunities Development`, `Applications Development`, `Trends Evaluation and Application`, `Documentation`

## IE4213 Learning from Data

Original extracted skills:
```text
Data Engineering | Engineering Problem Solving | Data and Statistical Analytics | Big Data Analytics | Business Data Analysis | Data Design | Data Visualisation | Quality Engineering | Pattern Recognition Systems | Data Sharing
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The module suggests some coverage through engineer, but it does not fully confirm the full taxonomy definition. |
| Engineering Problem Solving | Apply the eight disciplines methodology for systematic problem solving including root cause analysis, failure mode effect and analysis, containment actions, and corrective actions and preventive actions in accordance with organisational systems and processes | manual review | The module suggests some coverage through engineer, problem, solv, but it does not fully confirm the full taxonomy definition. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Quality Engineering | Create, deploy and maintain quality-related systems, processes and tools to establish an environment that supports process and product quality | manual review | The module suggests some coverage through engineer, but it does not fully confirm the full taxonomy definition. |
| Pattern Recognition Systems | Develop and apply intelligent pattern recognition systems and techniques to analyse data and derive useful hidden patterns to solve problems | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Sharing | Assess the value of data to achieve a competitive advantage and business objectives | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: None

Manual review skills: `Data Engineering`, `Engineering Problem Solving`, `Data and Statistical Analytics`, `Big Data Analytics`, `Business Data Analysis`, `Data Design`, `Data Visualisation`, `Quality Engineering`, `Pattern Recognition Systems`, `Data Sharing`

## IE4251 Process Analysis and Redesign

Original extracted skills:
```text
Business Process Re-engineering | Business Process Management | Business Process Analysis | IT Strategy | Business Innovation | Continuous Quality Improvement | Infrastructure Support | Business Stakeholder Management | Innovation | Financial Analysis | Equipment and Systems Repair
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Business Process Re-engineering | Analyse business processes and workflows within the organisation and identification of new approaches to completely redesign business activities or optimise performance, quality and speed of services or processes including exploration of automating and streamlining processes, evaluation of associated costs and benefits of redesigning business processes, as well as identification of potential impact, change management activities and resources required | keep | The module description directly supports this skill through busines, engineer, proces. |
| Business Process Management | Manage and optimise an organisation's business processes for efficiency and effectiveness | keep | The module has direct support for this skill through busines, proces. |
| Business Process Analysis | Analyse business processes for improvement, optimisation and efficiency | keep | The module description directly supports this skill through analysi, busines, proces. |
| IT Strategy | Plan, develop and communicate effective inward- and outward-facing IT strategies, solutions and action plans, driven by environment scanning and assessment of the business' future needs and long-term strategic direction. This involves devising internal management strategies and models to support and sustain IT transformations and alignment of IT investments and programmes with the strategy to optimise the business value from IT | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Continuous Quality Improvement | Implement on-going efforts to improve products, services, and/or processes through leveraging on opportunities to streamline work, increase quality and reduce waste | keep | The module has direct support for this skill through improvement. |
| Infrastructure Support | Provide services to end users by systematically identifying, classifying and troubleshooting technical issues and incidents that disrupt and impact their day-to-day business activities, within a specified timeframe. This also includes implementing an end-to-end problem management process to analyse underlying problems, advising on infrastructure related upgrades and improvements and developing user guides and training materials | keep | The module description directly supports this skill through infrastructure. |
| Business Stakeholder Management | Establish mutually beneficial relationships with business partners and stakeholders including potential customers and financing partners | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Innovation | Foster a culture of innovation across the organisation through ideation thereby enhancing efficiency and productivity | remove | The module title/description centers on `Process Analysis and Redesign` rather than `Innovation` as defined in the taxonomy. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Equipment and Systems Repair | Execute equipment and systems repair procedures to correct faults and restore functionalities | remove | The module title/description centers on `Process Analysis and Redesign` rather than `Equipment and Systems Repair` as defined in the taxonomy. |

Proposed cleaned skills: `Business Process Re-engineering`, `Business Process Management`, `Business Process Analysis`, `Continuous Quality Improvement`, `Infrastructure Support`

Manual review skills: `IT Strategy`, `Business Innovation`, `Business Stakeholder Management`, `Financial Analysis`

## IPM3101 Project Feasibility

Original extracted skills:
```text
Project Plan | Project Feasibility Assessment | Design Creation and Development | Property Operations Management | Site Assessment and Analysis | Project Integration | Infrastructure Strategy | Cost Management | Project Cost | Applications Development | Market Research
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Project Feasibility Assessment | Study project feasibility to meet project outcomes and objectives | keep | The module has direct support for this skill through feasibility. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Property Operations Management | Manage property operations and evaluate operational results to ensure operational efficiency and high service standards to enhance guest experience | remove | The module title/description centers on `Project Feasibility` rather than `Property Operations Management` as defined in the taxonomy. |
| Site Assessment and Analysis | Plan and execute assessments of project sites to evaluate suitability for built environment operations | remove | The taxonomy description is specific to construction/BIM, which is not reflected in the module. |
| Project Integration | Set programme direction as well as balance overall project management functions across the project life cycle | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Infrastructure Strategy | Develop a robust strategy and plan for defining and managing a future-ready IT infrastructure, optimising its capacity, availability and synchronisation to enable an organisation's business operations. This involves evaluating infrastructure models and options for infrastructure components, managing infrastructure investments and facilitating the transformation toward the desired future infrastructure model | manual review | The module suggests some coverage through infrastructure, but it does not fully confirm the full taxonomy definition. |
| Cost Management | Analyse, plan and manage costs for cost efficiency and expense reduction | manual review | The module suggests some coverage through cost, but it does not fully confirm the full taxonomy definition. |
| Project Cost | Set budgets, monitor costs and assess budget implications of projects on operations | keep | The module description directly supports this skill through cost. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | Feasibility, site study, and project brief work do not imply app development. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Project Feasibility Assessment`, `Project Cost`

Manual review skills: `Project Plan`, `Design Creation and Development`, `Project Integration`, `Infrastructure Strategy`, `Cost Management`, `Market Research`

## IPM3103 Project Finance

Original extracted skills:
```text
Financial Modelling | Capital Management | Project Cost | Project Plan | Financial Budgeting | Sustainable Lending Instruments Structuring | Financial Statements Analysis | Project Coordination | Financial Administration | Carbon Credit Project Development | Risk Assessment | Financial Transactions | Valuation
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | keep | The module description directly supports this skill through finance. |
| Capital Management | Calculate capital adequacy ratios to determine capital buffers necessary for the bank or financial institution, while optimising returns on capital based on capital allocation strategies | manual review | The module suggests some coverage through capital, but it does not fully confirm the full taxonomy definition. |
| Project Cost | Set budgets, monitor costs and assess budget implications of projects on operations | keep | The module description directly supports this skill through cost. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | keep | The module description directly supports this skill through plan. |
| Financial Budgeting | Prepare organisational budgets to support short- and long-term business plans through forecasting, allocation and financial policy settings | manual review | The module suggests some coverage through budget, finance, but it does not fully confirm the full taxonomy definition. |
| Sustainable Lending Instruments Structuring | Structure key sustainable lending instruments, which includes bonds, loans, project and trade financing, derivatives, blended finance and develop incentive mechanism to encourage adoption of these instruments | manual review | The module suggests some coverage through structur, sustainable, but it does not fully confirm the full taxonomy definition. |
| Financial Statements Analysis | Analyse financial statements in accordance with the applicable frameworks | keep | The module description directly supports this skill through analysi, finance, statement. |
| Project Coordination | Coordinate project activities and workflows in collaboration with project teams and relevant stakeholders, as determined by project plans, to fulfil expected project outcomes and objectives | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Administration | Ensure healthy finance to aid business growth and operations | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Carbon Credit Project Development | Analyse and identify carbon credit projects that generate carbon credits. Assess the feasibility and financial implications of projects and ensure carbon credit projects comply with carbon standards and methodologies, demonstrating additionality through estimated emissions reductions. Design and develop carbon credit projects that effectively reduce, remove, avoid and store greenhouse gas (GHG) emissions, in compliance with applicable carbon crediting standards, for the eventual issuance for carbon credits for future trading by the organisation. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Risk Assessment | Perform assessment of risks, including fraud risks, through understanding the client's business | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Valuation | Perform valuation for business and financial assets for deal structuring | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Financial Modelling`, `Project Cost`, `Project Plan`, `Financial Statements Analysis`, `Risk Assessment`

Manual review skills: `Capital Management`, `Financial Budgeting`, `Sustainable Lending Instruments Structuring`, `Project Coordination`, `Financial Administration`, `Carbon Credit Project Development`, `Financial Transactions`, `Valuation`

## IS3150 Digital Media Marketing

Original extracted skills:
```text
Digital Marketing Management | Social Media Marketing | Integrated Marketing | Brand Management | Customer Management | Public Relations Management | Innovation | Creative Storytelling | Search Engine Optimisation (SEO) | Trading Analysis | Display Creation and Management
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Digital Marketing Management | Perform digital marketing activities, including Search Engine Optimisation (SEO), Search Engine Marketing (SEM) and affiliate marketing | keep | The module has direct support for this skill through digital, market. |
| Social Media Marketing | Formulate, execute and evaluate social media strategic plans to establish positive relationships with industry and social media colleagues and proactively seek and evaluate innovative marketing opportunities | keep | The module description directly supports this skill through market, media, social. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Brand Management | Co-create the organisation's projected brand and reputation with the customer, consider customer's perspectives and the organisation's desired image and priorities. This also includes the development and execution of branding campaigns, public relations and reputation management strategies to sustain or enhance the desired brand | keep | The module has direct support for this skill through brand. |
| Customer Management | Manage customers with the goal of improving business relationships with customers and achieving service requirements | manual review | The module suggests some coverage through customer, but it does not fully confirm the full taxonomy definition. |
| Public Relations Management | Formulate and oversee organisations' public relations (PR) strategies and plans | keep | The module has direct support for this skill through public, relation. |
| Innovation | Foster a culture of innovation across the organisation through ideation thereby enhancing efficiency and productivity | manual review | The module suggests some coverage through innovation, but it does not fully confirm the full taxonomy definition. |
| Creative Storytelling | Convey stories, ideas or concepts in a compelling and engaging manner through creative mediums | manual review | The module suggests some coverage through storytell, but it does not fully confirm the full taxonomy definition. |
| Search Engine Optimisation (SEO) | Optimise online digital assets and content of brands and products to enable and enhance discoverability by search engines | manual review | The module suggests some coverage through engine, search, but it does not fully confirm the full taxonomy definition. |
| Trading Analysis | Develop market research reports to support trading strategies | keep | The module has direct support for this skill through analysi. |
| Display Creation and Management | Conceive, design and implement plant and merchandise displays to enhance their visibility and promote nursery sales | remove | The taxonomy description is specific to retail/merchandising, which is not reflected in the module. |

Proposed cleaned skills: `Digital Marketing Management`, `Social Media Marketing`, `Brand Management`, `Public Relations Management`, `Trading Analysis`

Manual review skills: `Integrated Marketing`, `Customer Management`, `Innovation`, `Creative Storytelling`, `Search Engine Optimisation (SEO)`

## IS4100 IT Project Management

Original extracted skills:
```text
Project Management | Project Execution and Control | Project Administration | Project Plan | Project Coordination | Information Technology Application Support and Monitoring | Applications Development | Network Simulation and Analysis | Portfolio Management | Computational Modelling
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Project Management | Execute projects by managing stakeholder engagement, resources, budgets and resolving problems | keep | Project management is the core focus of the module. |
| Project Execution and Control | Implement projects in accordance with project plan and deliverables, and monitoring and controlling processes performed to influence project outcomes | keep | Execution and control are direct project-management topics. |
| Project Administration | Plan and coordinate project closures and documentation processes, and refine project administration policies and procedures | keep | Project administration aligns directly with the module. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | keep | Project planning is directly supported. |
| Project Coordination | Coordinate project activities and workflows in collaboration with project teams and relevant stakeholders, as determined by project plans, to fulfil expected project outcomes and objectives | keep | Project coordination is part of the module scope. |
| Information Technology Application Support and Monitoring | Provide Information Technology (IT) application and security support by troubleshooting issues, identifying root causes, performing trend analysis and/or monitoring performance, to ensure issues are resolved. | manual review | Monitoring/control are present, but operational app-support work is not central. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | The module is about project management rather than building software. |
| Network Simulation and Analysis | Analyse the natural gas network to coordinate bookings of available capacities, maintain optimal performance settings and drive enhancements to the network | remove | The taxonomy entry is network-engineering specific, not IT project management. |
| Portfolio Management | Manage systematically the IT investments, projects, services and activities within a company, in line with business objectives and priorities. This involves the development of a framework to evaluate potential costs and benefits and make key decisions about IT investments, internal allocation and utilisation of IT resources and/or assets and any changes to IT processes or services offered | keep | Project evaluation and selection in an IT context support this skill. |
| Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks. This also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issues or requirements | remove | The module may use planning tools, but it is not a computational-modelling course. |

Proposed cleaned skills: `Project Management`, `Project Execution and Control`, `Project Administration`, `Project Plan`, `Project Coordination`, `Portfolio Management`

Manual review skills: `Information Technology Application Support and Monitoring`

## IS4108 AI Solutioning Capstone Project

Original extracted skills:
```text
Artificial Intelligence Application | Governance | Agile Software Development | Solution Architecture | Software Design | Applications Development | Solutions Design Thinking | Responsible AI and Generative AI Practices | Ethical Culture | Organisational Strategy and Policy Realisation | Prompt Engineering | Data Strategy | Quality Standards
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | keep | Developing a business AI solution is central to the capstone. |
| Governance | Evaluate and improve governance practices in the organisation | keep | AI governance is explicitly named. |
| Agile Software Development | Plan and implement Agile methodology and the use of adaptive and iterative methods and techniques in the software development lifecycle to account for continuous evolution, development, and deployment to enable seamless delivery of the application to the end user | keep | Modern agile methodologies are explicitly part of the module. |
| Solution Architecture | Design or refine a solution blueprint or structure to guide the development of IT solutions in hardware, software, processes or related components, to meet current and future business needs. The solution architecture developed may lead to broad or specific changes to IT services, operating models and processes, and should provide a framework to guide the development and modification of solutions | keep | Devising viable integrated AI solutions directly supports solution architecture. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | keep | Software applications integrated with AI models are explicit module topics. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | keep | Implementing the AI solution directly supports applications development. |
| Solutions Design Thinking | Construct solution based upon logic, imagination, intuition, and systemic reasoning, to explore possibilities of what can be and create desired outcomes that benefit the organisation and customers | remove | The taxonomy description is specific to construction/BIM, which is not reflected in the module. |
| Responsible AI and Generative AI Practices | Integrate and ensure compliance of ethical principles in AI projects. Drive framework creation for responsible AI development. | keep | AI governance and ethics are explicit module topics. |
| Ethical Culture | Evaluate and foster strong ethical climate | manual review | Ethics is explicit, but organisation-wide culture-building is broader than the capstone. |
| Organisational Strategy and Policy Realisation | Making management decisions to establish, review and refine strategic organisational objectives and policies through collation and analysis of relevant organisational and business information | remove | The module is about delivering AI solutions, not setting organisational policy. |
| Prompt Engineering | Create nuanced and strategic prompts that optimise AI model performance, combining different methodologies to generate innovative and effective prompts. | manual review | The GenAI context makes this plausible, but prompt engineering is not named explicitly. |
| Data Strategy | Develop a robust and coherent data strategy and support architectures, policies, practices and procedures that enable the organisation to manage and utilise data in an effective manner. This includes introduction of innovative ways of organising, managing and integrating the data of the organisation to ensure their viability and ability to drive business value. It also includes the setting of information storage, sharing, handling and usage protocols to support alignment with relevant legislation and business strategies | manual review | DataOps and MLOps make this plausible, but enterprise data strategy is not explicit. |
| Quality Standards | Develop, review and communicate a clear, quality expectations and standards within an organisation that are aligned to the company's values and business objectives. This encompasses the setting and implementation of quality expectations for IT products and services delivered to both internal or external clients | manual review | Best practices and delivery quality are implied, but standards-setting is broader than the module. |

Proposed cleaned skills: `Artificial Intelligence Application`, `Governance`, `Agile Software Development`, `Solution Architecture`, `Software Design`, `Applications Development`, `Responsible AI and Generative AI Practices`

Manual review skills: `Ethical Culture`, `Prompt Engineering`, `Data Strategy`, `Quality Standards`

## IS4204 IT Governance

Original extracted skills:
```text
Operation Management | IT Asset Management | IT Strategy | Business Continuity Management | Risk Management | Programme and Project Management | Security Strategy | Quality System Management | Sustainable Investment Management | Strategy Planning | Portfolio Management
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Operation Management | Manage organisation's operational effectiveness and efficiency in accordance with regulatory frameworks and requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| IT Asset Management | Manage, optimise and protect the organisation's IT assets. This includes the timely purchase, deployment, categorisation, maintenance and phase out of IT assets within the organisation in a way that optimises business value. Also includes development and implementation of procedures to guide the proper handling, usage and storage of IT assets to limit potential business or legal risks | manual review | The skill is plausible in an IT-governance context, but asset lifecycle handling is not explicit. |
| IT Strategy | Plan, develop and communicate effective inward- and outward-facing IT strategies, solutions and action plans, driven by environment scanning and assessment of the business' future needs and long-term strategic direction. This involves devising internal management strategies and models to support and sustain IT transformations and alignment of IT investments and programmes with the strategy to optimise the business value from IT | keep | IT strategy is explicitly named in the module description. |
| Business Continuity Management | Develop business continuity strategies to manage risks in response to disruptive events | keep | Business continuity is explicitly named in the module description. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | Risk management is an explicit topic. |
| Programme and Project Management | Manage the implementation and development of programmes and projects to facilitate achievement of organisation's objectives and growth. | keep | Programme and project management are explicit module topics. |
| Security Strategy | Establish the organisation's security vision, strategy and initiatives to ensure adequate protection of assets. This involves the planning, implementation and review of enterprise-wide security controls which includes policies, processes, physical infrastructure, software and hardware functions to govern and preserve the privacy, security and confidentiality of the organisation's information and assets | keep | Security strategy is explicitly named in the module description. |
| Quality System Management | Coordinate and direct the organisation's activities to meet customer and regulatory requirements as well as identify opportunities for improvement. | manual review | Quality management is relevant, but the taxonomy definition is broader. |
| Sustainable Investment Management | Lead organisation's strategies on sustainable investment and implement sustainable investment concepts and approaches on portfolio management | remove | The module is about IT governance rather than sustainable investment. |
| Strategy Planning | Develop organisational strategies and policies by analysing the impact of internal and external influencing factors and seeking consultation from relevant stakeholders. | keep | Strategic planning is directly supported. |
| Portfolio Management | Manage systematically the IT investments, projects, services and activities within a company, in line with business objectives and priorities. This involves the development of a framework to evaluate potential costs and benefits and make key decisions about IT investments, internal allocation and utilisation of IT resources and/or assets and any changes to IT processes or services offered | keep | Portfolio management is an explicit module topic. |

Proposed cleaned skills: `IT Strategy`, `Business Continuity Management`, `Risk Management`, `Programme and Project Management`, `Security Strategy`, `Strategy Planning`, `Portfolio Management`

Manual review skills: `Operation Management`, `IT Asset Management`, `Quality System Management`

## LSM3257 Applied Data Analysis in Ecology and Evolution

Original extracted skills:
```text
Ecology in Landscapes | Environment Observation | Data Collection and Analysis | Sustainability Management | Data Analysis and Interpretation | Data Collection and Management | Data Visualisation | Measurement, Reporting and Verification (MRV) (For Carbon Credit Projects) | Learning Analytics | Management Decision Making | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Ecology in Landscapes | Adopt principles of ecology in the design, implementation and management of landscapes | keep | The module has direct support for this skill through ecology. |
| Environment Observation | Measure situations by discerning the environment | manual review | The module suggests some coverage through environment, but it does not fully confirm the full taxonomy definition. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | keep | The module description directly supports this skill through analysi, collection. |
| Sustainability Management | Plan, develop and roll out of an organisation-wide sustainability strategy. This includes the assessment of the organisation's utilisation and/or consumption of energy and other resources, vis-a-vis the availability and stability of supply sources and external best practices and standards in sustainability. This also includes the on-going monitoring and tracking of energy and/or resource-consumption over time, to identify impact on the organisation's internal and external environment as well as potential improvements in energy- or resource-efficiency. | manual review | The module suggests some coverage through sustainability, but it does not fully confirm the full taxonomy definition. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module has direct support for this skill through analysi. |
| Data Collection and Management | Employ sound research methodologies to collect and manage data | keep | The module has direct support for this skill through collection. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Measurement, Reporting and Verification (MRV) (For Carbon Credit Projects) | Systematically collect, quantify, report and verify data related to greenhouse gas (GHG) emissions and other environmental metrics stemming from carbon credit projects. Ensure data quality and accuracy to ascertain the integrity of carbon projects and compliance with carbon standards. | manual review | The module suggests some coverage through report, but it does not fully confirm the full taxonomy definition. |
| Learning Analytics | Analyse data to glean insights and drive decision making to enhance learning delivery, in accordance with governance and management policies for the handling of data at various stages of its lifecycle. | keep | The module description directly supports this skill through learn. |
| Management Decision Making | Make financial decisions based on management reports | keep | The module has direct support for this skill through decision, mak. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Ecology in Landscapes`, `Data Collection and Analysis`, `Data Analysis and Interpretation`, `Data Collection and Management`, `Learning Analytics`, `Management Decision Making`

Manual review skills: `Environment Observation`, `Sustainability Management`, `Data Visualisation`, `Measurement, Reporting and Verification (MRV) (For Carbon Credit Projects)`, `Financial Analysis`

## ME2102 Engineering Innovation and Modelling

Original extracted skills:
```text
Engineering Drawing and Design Specifications | Engineering Drawing, Interpretation and Management | 3D Modelling | Joining and Welding | Mechanical Engineering Management | Materials Qualification | Manual and Digital Drawings Production | Applications Development | Component Assembly | Geometric Dimensioning and Tolerancing
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Engineering Drawing and Design Specifications | Create design specifications and technical drawings to guide installation and construction works | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to construction/BIM than the module makes clear. |
| Engineering Drawing, Interpretation and Management | Use engineering drawings and documentation describing layout, location, interconnection, design and operational parameters, and operating and safety design limits to support engineering activities | keep | The module has direct support for this skill through draw, engineer. |
| 3D Modelling | Generate 3D models using a variety of modelling software to represent characteristics of a real-world system | keep | The module description directly supports this skill through 3d. |
| Joining and Welding | Perform welding operations using appropriate tools, equipment, materials and methods in accordance with applicable technical manuals and organisational procedures. | keep | The module description directly supports this skill through join, weld. |
| Mechanical Engineering Management | Manage the design, technical specification, selection, modification and troubleshooting of mechanical equipment, structures and systems so as to provide mechanical engineering discipline support to construction, operations, maintenance and project teams | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to construction/BIM than the module makes clear. |
| Materials Qualification | Manage the quality of materials to ensure material specifications conform to product requirements | keep | The module has direct support for this skill through material. |
| Manual and Digital Drawings Production | Develop drawing requirements, evaluate drawing conventions and specifications, as well as identify production materials and methods | manual review | The module suggests some coverage through drawing, but it does not fully confirm the full taxonomy definition. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | The module title/description centers on `Engineering Innovation and Modelling` rather than `Applications Development` as defined in the taxonomy. |
| Component Assembly | Produce structures from smaller components by interpreting hull structure drawings, mechanical equipment drawings, electrical drawings and other technical drawings applicable to marine equipment, ships, rigs and conversions | remove | The course covers CAD/specification work, not marine component assembly. |
| Geometric Dimensioning and Tolerancing | Define and verify acceptable engineering tolerances of products' and parts' geometry | keep | The module description directly supports this skill through dimension, geometric, toleranc. |

Proposed cleaned skills: `Engineering Drawing, Interpretation and Management`, `3D Modelling`, `Joining and Welding`, `Materials Qualification`, `Geometric Dimensioning and Tolerancing`

Manual review skills: `Engineering Drawing and Design Specifications`, `Mechanical Engineering Management`, `Manual and Digital Drawings Production`

## ME4263 Fundamentals of Product Development

Original extracted skills:
```text
Engineering Product Design | Product Testing | Design for Manufacturing and Assembly | Digital and Physical Prototyping | Product Demonstration | Business Needs Analysis | Design Writing | Applications Development | Technical Sales Support | Conceptual Thinking | Design for Maintainability
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Engineering Product Design | Facilitate the design of products to meet requirements for functionality and performance | keep | The module has direct support for this skill through product. |
| Product Testing | Test biopharmaceutical products to verify that they have been produced to the required quality and regulatory standards | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to biopharma than the module makes clear. |
| Design for Manufacturing and Assembly | Apply Design for Manufacturing and Assembly (DfMA) principles throughout construction project lifecycle to ensure effectiveness, safety and economies of scale for manufacturing and assembly | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to construction/BIM than the module makes clear. |
| Digital and Physical Prototyping | Construct design concepts, either digitally or physically, to develop deeper understanding of the designs and test their usability and functionality | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to construction/BIM than the module makes clear. |
| Product Demonstration | Develop knowledge of the range and price of the organisation's products and services, as well as present and demonstrate the use and application of products and services to customers | manual review | The module suggests some coverage through product, but it does not fully confirm the full taxonomy definition. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | remove | The module title/description centers on `Fundamentals of Product Development` rather than `Business Needs Analysis` as defined in the taxonomy. |
| Design Writing | Convey a design story, idea or concept in a compelling and engaging manner through writing | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Technical Sales Support | Develop preliminary technical solutions, proposal or initial prototypes to address customers' needs. This includes analysis and diagnosis of customers' technical requirements, design of proof of concept, and delivery of product demonstrations and/or customisation samples as part of broader end-to-end solution to customers | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Conceptual Thinking | Analyse and synthesise information by identifying key issues, perceiving unseen patterns and trends and deducing connections between issues to develop relevant ideas and solutions | manual review | The module suggests some coverage through conceptual, but it does not fully confirm the full taxonomy definition. |
| Design for Maintainability | Apply Design for Maintainability (DfM) principles throughout the project lifecycle to ensure effectiveness, safety and economies of scale for maintenance tasks | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Engineering Product Design`

Manual review skills: `Product Testing`, `Design for Manufacturing and Assembly`, `Digital and Physical Prototyping`, `Product Demonstration`, `Design Writing`, `Applications Development`, `Technical Sales Support`, `Conceptual Thinking`, `Design for Maintainability`

## MKT3415 Digital Marketing

Original extracted skills:
```text
Digital Marketing and Communication | Affiliate Marketing | Customer Behaviour Analysis | E-commerce Management | Consumer Intelligence Analysis | Marketing Strategy | Business Relationship Building | Business Innovation | IT Strategy | Merchandise Buying | Financial Transactions
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Digital Marketing and Communication | Develop digital outreach plans and marketing collaterals to communicate and enhance the organisation's employer brand | manual review | The module suggests some coverage through digital, market, but it does not fully confirm the full taxonomy definition. |
| Affiliate Marketing | Select and manage affiliates to strengthen customer engagement, enhance lead conversion, broaden the reach of marketing efforts and optimise marketing return-on-investment | keep | Affiliate marketing is explicitly named in the module description. |
| Customer Behaviour Analysis | Devise customer behaviour analysis tools and approaches, to perform analysis on information pertaining to customer behaviours, leading to improved customer recommendations | keep | The module has direct support for this skill through analysi, customer. |
| E-commerce Management | Develop, manage and execute e-commerce strategies and activities according to organisational objectives | keep | Internet shopping, e-tailing, and e-business are core module topics. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | keep | The module has direct support for this skill through analysi, consumer. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Business Relationship Building | Formulate business partnership strategies and establish relevant networks of strategic partners that provide value to the organisation | manual review | The module suggests some coverage through busines, relationship, but it does not fully confirm the full taxonomy definition. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| IT Strategy | Plan, develop and communicate effective inward- and outward-facing IT strategies, solutions and action plans, driven by environment scanning and assessment of the business' future needs and long-term strategic direction. This involves devising internal management strategies and models to support and sustain IT transformations and alignment of IT investments and programmes with the strategy to optimise the business value from IT | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Merchandise Buying | Design and implement merchandise buying plans according to market and consumer trends, merchandise ranges, stock levels and sources of supply | remove | Digital marketing does not directly support merchandise-buying planning. |
| Financial Transactions | Prepare business documentation and cash balances | remove | The syllabus does not support cash-balance or transaction-document work. |

Proposed cleaned skills: `Affiliate Marketing`, `Customer Behaviour Analysis`, `E-commerce Management`, `Consumer Intelligence Analysis`

Manual review skills: `Digital Marketing and Communication`, `Marketing Strategy`, `Business Relationship Building`, `Business Innovation`, `IT Strategy`

## MKT3416 Business-to-Business Marketing

Original extracted skills:
```text
Marketing Strategy Development | Marketing Management | Business-to-Business Customer Relationship Management | Marketing Strategy | Product Marketing and Branding | Integrated Marketing | Customer Relationship Management Operations | Market Research | Competitive Business Strategy | Product Management | Market Entry Strategy Formulation | Business Innovation | Business Negotiation | Pricing Strategy | Customer Service Delivery | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | keep | Business market strategy formulation is explicitly covered. |
| Marketing Management | Manage organisation's marketing plans | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Business-to-Business Customer Relationship Management | Manage relationships with stakeholders for account management, retention and business development purposes | keep | The module description directly supports this skill through busines, customer, relationship. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module description directly supports this skill through market. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | manual review | The module suggests some coverage through market, product, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | keep | The module has direct support for this skill through market. |
| Customer Relationship Management Operations | Manage and analyse customer data to foster long-term relationships with customers and drive sales growth | keep | The module description directly supports this skill through customer, relationship. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module has direct support for this skill through market. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation | keep | Competitor analysis and business-market strategy formulation are explicit module topics. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Market Entry Strategy Formulation | Develop strategic plans to enter identified markets based on assessed costs, benefits and risks involved | keep | The module description directly supports this skill through formulation, market. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Business Negotiation | Conduct negotiations to establish win-win outcomes for the organisation | keep | Customer negotiations are explicitly listed topics. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy Development`, `Marketing Management`, `Business-to-Business Customer Relationship Management`, `Marketing Strategy`, `Integrated Marketing`, `Customer Relationship Management Operations`, `Market Research`, `Competitive Business Strategy`, `Product Management`, `Market Entry Strategy Formulation`, `Business Negotiation`, `Pricing Strategy`

Manual review skills: `Product Marketing and Branding`, `Business Innovation`, `Financial Analysis`

## MKT3416A Business-to-Business Marketing

Original extracted skills:
```text
Marketing Strategy Development | Marketing Management | Business-to-Business Customer Relationship Management | Marketing Strategy | Product Marketing and Branding | Integrated Marketing | Customer Relationship Management Operations | Market Research | Competitive Business Strategy | Product Management | Market Entry Strategy Formulation | Business Innovation | Business Negotiation | Pricing Strategy | Customer Service Delivery | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | keep | Business market strategy formulation is explicitly covered. |
| Marketing Management | Manage organisation's marketing plans | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Business-to-Business Customer Relationship Management | Manage relationships with stakeholders for account management, retention and business development purposes | keep | The module description directly supports this skill through busines, customer, relationship. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module description directly supports this skill through market. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | manual review | The module suggests some coverage through market, product, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | keep | The module has direct support for this skill through market. |
| Customer Relationship Management Operations | Manage and analyse customer data to foster long-term relationships with customers and drive sales growth | keep | The module description directly supports this skill through customer, relationship. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module has direct support for this skill through market. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation | keep | Competitor analysis and business-market strategy formulation are explicit module topics. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Market Entry Strategy Formulation | Develop strategic plans to enter identified markets based on assessed costs, benefits and risks involved | keep | The module description directly supports this skill through formulation, market. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Business Negotiation | Conduct negotiations to establish win-win outcomes for the organisation | keep | Customer negotiations are explicitly listed topics. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy Development`, `Marketing Management`, `Business-to-Business Customer Relationship Management`, `Marketing Strategy`, `Integrated Marketing`, `Customer Relationship Management Operations`, `Market Research`, `Competitive Business Strategy`, `Product Management`, `Market Entry Strategy Formulation`, `Business Negotiation`, `Pricing Strategy`

Manual review skills: `Product Marketing and Branding`, `Business Innovation`, `Financial Analysis`

## MKT3416B Business-to-Business Marketing

Original extracted skills:
```text
Marketing Strategy Development | Marketing Management | Business-to-Business Customer Relationship Management | Marketing Strategy | Product Marketing and Branding | Integrated Marketing | Customer Relationship Management Operations | Market Research | Competitive Business Strategy | Product Management | Market Entry Strategy Formulation | Business Innovation | Business Negotiation | Pricing Strategy | Customer Service Delivery | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | keep | Business market strategy formulation is explicitly covered. |
| Marketing Management | Manage organisation's marketing plans | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Business-to-Business Customer Relationship Management | Manage relationships with stakeholders for account management, retention and business development purposes | keep | The module description directly supports this skill through busines, customer, relationship. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module description directly supports this skill through market. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | manual review | The module suggests some coverage through market, product, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | keep | The module has direct support for this skill through market. |
| Customer Relationship Management Operations | Manage and analyse customer data to foster long-term relationships with customers and drive sales growth | keep | The module description directly supports this skill through customer, relationship. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module has direct support for this skill through market. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation | keep | Competitor analysis and business-market strategy formulation are explicit module topics. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Market Entry Strategy Formulation | Develop strategic plans to enter identified markets based on assessed costs, benefits and risks involved | keep | The module description directly supports this skill through formulation, market. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Business Negotiation | Conduct negotiations to establish win-win outcomes for the organisation | keep | Customer negotiations are explicitly listed topics. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy Development`, `Marketing Management`, `Business-to-Business Customer Relationship Management`, `Marketing Strategy`, `Integrated Marketing`, `Customer Relationship Management Operations`, `Market Research`, `Competitive Business Strategy`, `Product Management`, `Market Entry Strategy Formulation`, `Business Negotiation`, `Pricing Strategy`

Manual review skills: `Product Marketing and Branding`, `Business Innovation`, `Financial Analysis`

## MKT3421 Marketing Analysis & Decision Making

Original extracted skills:
```text
Marketing Strategy | Market Research | Marketing Strategy Development | Product Marketing and Branding | Marketing Operations Management | Market Research and Analysis | Integrated Marketing | Cost Management | Customer Acquisition Management | Financial Analysis | New Product Introduction | Sales Target Management | Data Analysis and Interpretation | Software Design | Project Plan
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module has direct support for this skill through market. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module description directly supports this skill through market. |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to retail/merchandising than the module makes clear. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | keep | The module description directly supports this skill through brand, market, product. |
| Marketing Operations Management | Execute marketing tasks and activity operations | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Market Research and Analysis | Develop market analysis frameworks and objectives to guide and conduct analyses of market trends, developments, competitive factors and economic changes to identify useful business insights, drive economic decisions and forecast market needs | keep | The module description directly supports this skill through analysi, market. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Cost Management | Analyse, plan and manage costs for cost efficiency and expense reduction | keep | The module has direct support for this skill through cost. |
| Customer Acquisition Management | Develop customer acquisition strategies as well as foster customer relationships to attract new customers | manual review | The module suggests some coverage through customer, but it does not fully confirm the full taxonomy definition. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| New Product Introduction | Support new production by validating build plan to achieve cost-effective production and assembly as well as meeting design specifications | keep | The module has direct support for this skill through product. |
| Sales Target Management | Evaluate and monitor sales target and performance to plan and initiate actions to achieve excellence in sales delivery | manual review | The module suggests some coverage through target, but it does not fully confirm the full taxonomy definition. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module has direct support for this skill through analysi. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | remove | Spreadsheets and simulations support decisions, but this is not software design. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | manual review | The module suggests some coverage through plan, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy`, `Market Research`, `Product Marketing and Branding`, `Market Research and Analysis`, `Cost Management`, `New Product Introduction`, `Data Analysis and Interpretation`

Manual review skills: `Marketing Strategy Development`, `Marketing Operations Management`, `Integrated Marketing`, `Customer Acquisition Management`, `Financial Analysis`, `Sales Target Management`, `Project Plan`

## MKT3425 Retail Marketing

Original extracted skills:
```text
Retail Administration | Retailing and the Economy | Retail Space Utilisation | Visual Merchandising Presentation | Point-Of-Purchase Marketing | Store Facilities and Housekeeping | Pricing Strategy | Consumer Intelligence Analysis | Business Innovation | Enterprise Architecture
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Retail Administration | Manage and validate petty cash transactions, as well as document hours worked for each employee | remove | The taxonomy description is specific to HR/talent, which is not reflected in the module. |
| Retailing and the Economy | Anticipate and recognise shifts in the retail landscape, and demonstrate knowledge of the industry context within which the organisational operates in | manual review | The module suggests some coverage through retail, but it does not fully confirm the full taxonomy definition. |
| Retail Space Utilisation | Conceptualise and develop store and digital planograms which illustrate assortment of merchandise | manual review | The module suggests some coverage through retail, but it does not fully confirm the full taxonomy definition. |
| Visual Merchandising Presentation | Monitor accuracy of displays against visual merchandising display guidelines | keep | The module has direct support for this skill through merchandis, visual. |
| Point-Of-Purchase Marketing | Formulate in-store optimal offer strategies design optimal offer assortments and establish Point-of-Purchase (POP) set-up guidelines and promotion per POP to improve sales closures | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Store Facilities and Housekeeping | Identify facility and space requirements and negotiate contract terms and conditions to support business needs and volume | remove | The module title/description centers on `Retail Marketing` rather than `Store Facilities and Housekeeping` as defined in the taxonomy. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | remove | The module title/description centers on `Retail Marketing` rather than `Consumer Intelligence Analysis` as defined in the taxonomy. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | remove | Retail strategy and store management are much narrower than enterprise architecture. |

Proposed cleaned skills: `Visual Merchandising Presentation`, `Pricing Strategy`

Manual review skills: `Retailing and the Economy`, `Retail Space Utilisation`, `Point-Of-Purchase Marketing`, `Business Innovation`

## MKT3427 Research for Marketing Insights

Original extracted skills:
```text
Market Research | Market Research and Analysis | Research Design | Marketing Strategy | Integrated Marketing | Product Marketing and Branding | Business Data Analysis | Product Development | Data Collection and Analysis | Qualitative Research | Data Analysis and Interpretation | Report Writing | Arts Education Research
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module description directly supports this skill through market. |
| Market Research and Analysis | Develop market analysis frameworks and objectives to guide and conduct analyses of market trends, developments, competitive factors and economic changes to identify useful business insights, drive economic decisions and forecast market needs | keep | The module description directly supports this skill through analysi, market. |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | keep | The module has direct support for this skill through market, product. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Product Development | Evaluate consumer and market trends to determine value proposition, cost-effectiveness and profitability of proposed products in different markets | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | keep | The module description directly supports this skill through analysi, collection. |
| Qualitative Research | Conduct and lead qualitative research studies, focusing on the study of people, habits, norms and cultures, to uncover insights driving the behaviour of different respondents | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module has direct support for this skill through analysi. |
| Report Writing | Present specific information and evidence in a clear and structured format | keep | Report presentation and writing are explicit learning outcomes. |
| Arts Education Research | Investigate a research focus and hypothesis leading to the generation of insights on current developments, trends and innovative methods of learning delivery and programme design. | remove | This is marketing research, not arts-education research. |

Proposed cleaned skills: `Market Research`, `Market Research and Analysis`, `Research Design`, `Product Marketing and Branding`, `Product Development`, `Data Collection and Analysis`, `Data Analysis and Interpretation`, `Report Writing`

Manual review skills: `Marketing Strategy`, `Integrated Marketing`, `Business Data Analysis`, `Qualitative Research`

## MKT3714 Digital Marketing

Original extracted skills:
```text
Digital Marketing and Communication | Affiliate Marketing | Customer Behaviour Analysis | E-commerce Management | Consumer Intelligence Analysis | Marketing Strategy | Business Relationship Building | Business Innovation | IT Strategy | Merchandise Buying | Financial Transactions
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Digital Marketing and Communication | Develop digital outreach plans and marketing collaterals to communicate and enhance the organisation's employer brand | manual review | The module suggests some coverage through digital, market, but it does not fully confirm the full taxonomy definition. |
| Affiliate Marketing | Select and manage affiliates to strengthen customer engagement, enhance lead conversion, broaden the reach of marketing efforts and optimise marketing return-on-investment | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to marine/offshore than the module makes clear. |
| Customer Behaviour Analysis | Devise customer behaviour analysis tools and approaches, to perform analysis on information pertaining to customer behaviours, leading to improved customer recommendations | keep | The module has direct support for this skill through analysi, customer. |
| E-commerce Management | Develop, manage and execute e-commerce strategies and activities according to organisational objectives | manual review | The module suggests some coverage through e, but it does not fully confirm the full taxonomy definition. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | keep | The module has direct support for this skill through analysi, consumer. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Business Relationship Building | Formulate business partnership strategies and establish relevant networks of strategic partners that provide value to the organisation | manual review | The module suggests some coverage through busines, relationship, but it does not fully confirm the full taxonomy definition. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| IT Strategy | Plan, develop and communicate effective inward- and outward-facing IT strategies, solutions and action plans, driven by environment scanning and assessment of the business' future needs and long-term strategic direction. This involves devising internal management strategies and models to support and sustain IT transformations and alignment of IT investments and programmes with the strategy to optimise the business value from IT | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Merchandise Buying | Design and implement merchandise buying plans according to market and consumer trends, merchandise ranges, stock levels and sources of supply | remove | The apparent match is driven by generic wording, while the taxonomy entry is really about retail/merchandising. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Customer Behaviour Analysis`, `Consumer Intelligence Analysis`

Manual review skills: `Digital Marketing and Communication`, `Affiliate Marketing`, `E-commerce Management`, `Marketing Strategy`, `Business Relationship Building`, `Business Innovation`, `IT Strategy`, `Financial Transactions`

## MKT3714A Digital Marketing

Original extracted skills:
```text
Digital Marketing and Communication | Affiliate Marketing | Customer Behaviour Analysis | E-commerce Management | Consumer Intelligence Analysis | Marketing Strategy | Business Relationship Building | Business Innovation | IT Strategy | Merchandise Buying | Financial Transactions
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Digital Marketing and Communication | Develop digital outreach plans and marketing collaterals to communicate and enhance the organisation's employer brand | manual review | The module suggests some coverage through digital, market, but it does not fully confirm the full taxonomy definition. |
| Affiliate Marketing | Select and manage affiliates to strengthen customer engagement, enhance lead conversion, broaden the reach of marketing efforts and optimise marketing return-on-investment | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to marine/offshore than the module makes clear. |
| Customer Behaviour Analysis | Devise customer behaviour analysis tools and approaches, to perform analysis on information pertaining to customer behaviours, leading to improved customer recommendations | keep | The module has direct support for this skill through analysi, customer. |
| E-commerce Management | Develop, manage and execute e-commerce strategies and activities according to organisational objectives | manual review | The module suggests some coverage through e, but it does not fully confirm the full taxonomy definition. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | keep | The module has direct support for this skill through analysi, consumer. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Business Relationship Building | Formulate business partnership strategies and establish relevant networks of strategic partners that provide value to the organisation | manual review | The module suggests some coverage through busines, relationship, but it does not fully confirm the full taxonomy definition. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| IT Strategy | Plan, develop and communicate effective inward- and outward-facing IT strategies, solutions and action plans, driven by environment scanning and assessment of the business' future needs and long-term strategic direction. This involves devising internal management strategies and models to support and sustain IT transformations and alignment of IT investments and programmes with the strategy to optimise the business value from IT | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Merchandise Buying | Design and implement merchandise buying plans according to market and consumer trends, merchandise ranges, stock levels and sources of supply | remove | The apparent match is driven by generic wording, while the taxonomy entry is really about retail/merchandising. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Customer Behaviour Analysis`, `Consumer Intelligence Analysis`

Manual review skills: `Digital Marketing and Communication`, `Affiliate Marketing`, `E-commerce Management`, `Marketing Strategy`, `Business Relationship Building`, `Business Innovation`, `IT Strategy`, `Financial Transactions`

## MKT3714B Digital Marketing

Original extracted skills:
```text
Digital Marketing and Communication | Affiliate Marketing | Customer Behaviour Analysis | E-commerce Management | Consumer Intelligence Analysis | Marketing Strategy | Business Relationship Building | Business Innovation | IT Strategy | Merchandise Buying | Financial Transactions
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Digital Marketing and Communication | Develop digital outreach plans and marketing collaterals to communicate and enhance the organisation's employer brand | manual review | The module suggests some coverage through digital, market, but it does not fully confirm the full taxonomy definition. |
| Affiliate Marketing | Select and manage affiliates to strengthen customer engagement, enhance lead conversion, broaden the reach of marketing efforts and optimise marketing return-on-investment | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to marine/offshore than the module makes clear. |
| Customer Behaviour Analysis | Devise customer behaviour analysis tools and approaches, to perform analysis on information pertaining to customer behaviours, leading to improved customer recommendations | keep | The module has direct support for this skill through analysi, customer. |
| E-commerce Management | Develop, manage and execute e-commerce strategies and activities according to organisational objectives | manual review | The module suggests some coverage through e, but it does not fully confirm the full taxonomy definition. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | keep | The module has direct support for this skill through analysi, consumer. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Business Relationship Building | Formulate business partnership strategies and establish relevant networks of strategic partners that provide value to the organisation | manual review | The module suggests some coverage through busines, relationship, but it does not fully confirm the full taxonomy definition. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| IT Strategy | Plan, develop and communicate effective inward- and outward-facing IT strategies, solutions and action plans, driven by environment scanning and assessment of the business' future needs and long-term strategic direction. This involves devising internal management strategies and models to support and sustain IT transformations and alignment of IT investments and programmes with the strategy to optimise the business value from IT | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Merchandise Buying | Design and implement merchandise buying plans according to market and consumer trends, merchandise ranges, stock levels and sources of supply | remove | The apparent match is driven by generic wording, while the taxonomy entry is really about retail/merchandising. |
| Financial Transactions | Prepare business documentation and cash balances | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Customer Behaviour Analysis`, `Consumer Intelligence Analysis`

Manual review skills: `Digital Marketing and Communication`, `Affiliate Marketing`, `E-commerce Management`, `Marketing Strategy`, `Business Relationship Building`, `Business Innovation`, `IT Strategy`, `Financial Transactions`

## MKT3715 Business-to-Business Marketing

Original extracted skills:
```text
Marketing Strategy Development | Marketing Management | Business-to-Business Customer Relationship Management | Marketing Strategy | Product Marketing and Branding | Integrated Marketing | Customer Relationship Management Operations | Market Research | Competitive Business Strategy | Product Management | Market Entry Strategy Formulation | Business Innovation | Business Negotiation | Pricing Strategy | Customer Service Delivery | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | keep | Business market strategy formulation is explicitly covered. |
| Marketing Management | Manage organisation's marketing plans | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Business-to-Business Customer Relationship Management | Manage relationships with stakeholders for account management, retention and business development purposes | keep | The module description directly supports this skill through busines, customer, relationship. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module description directly supports this skill through market. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | manual review | The module suggests some coverage through market, product, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | keep | The module has direct support for this skill through market. |
| Customer Relationship Management Operations | Manage and analyse customer data to foster long-term relationships with customers and drive sales growth | keep | The module description directly supports this skill through customer, relationship. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module has direct support for this skill through market. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation | keep | Competitor analysis and business-market strategy formulation are explicit module topics. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Market Entry Strategy Formulation | Develop strategic plans to enter identified markets based on assessed costs, benefits and risks involved | keep | The module description directly supports this skill through formulation, market. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Business Negotiation | Conduct negotiations to establish win-win outcomes for the organisation | keep | Customer negotiations are explicitly listed topics. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy Development`, `Marketing Management`, `Business-to-Business Customer Relationship Management`, `Marketing Strategy`, `Integrated Marketing`, `Customer Relationship Management Operations`, `Market Research`, `Competitive Business Strategy`, `Product Management`, `Market Entry Strategy Formulation`, `Business Negotiation`, `Pricing Strategy`

Manual review skills: `Product Marketing and Branding`, `Business Innovation`, `Financial Analysis`

## MKT3715A Business-to-Business Marketing

Original extracted skills:
```text
Marketing Strategy Development | Marketing Management | Business-to-Business Customer Relationship Management | Marketing Strategy | Product Marketing and Branding | Integrated Marketing | Customer Relationship Management Operations | Market Research | Competitive Business Strategy | Product Management | Market Entry Strategy Formulation | Business Innovation | Business Negotiation | Pricing Strategy | Customer Service Delivery | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | keep | Business market strategy formulation is explicitly covered. |
| Marketing Management | Manage organisation's marketing plans | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Business-to-Business Customer Relationship Management | Manage relationships with stakeholders for account management, retention and business development purposes | keep | The module description directly supports this skill through busines, customer, relationship. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module description directly supports this skill through market. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | manual review | The module suggests some coverage through market, product, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | keep | The module has direct support for this skill through market. |
| Customer Relationship Management Operations | Manage and analyse customer data to foster long-term relationships with customers and drive sales growth | keep | The module description directly supports this skill through customer, relationship. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module has direct support for this skill through market. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation | keep | Competitor analysis and business-market strategy formulation are explicit module topics. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Market Entry Strategy Formulation | Develop strategic plans to enter identified markets based on assessed costs, benefits and risks involved | keep | The module description directly supports this skill through formulation, market. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Business Negotiation | Conduct negotiations to establish win-win outcomes for the organisation | keep | Customer negotiations are explicitly listed topics. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy Development`, `Marketing Management`, `Business-to-Business Customer Relationship Management`, `Marketing Strategy`, `Integrated Marketing`, `Customer Relationship Management Operations`, `Market Research`, `Competitive Business Strategy`, `Product Management`, `Market Entry Strategy Formulation`, `Business Negotiation`, `Pricing Strategy`

Manual review skills: `Product Marketing and Branding`, `Business Innovation`, `Financial Analysis`

## MKT3715B Business-to-Business Marketing

Original extracted skills:
```text
Marketing Strategy Development | Marketing Management | Business-to-Business Customer Relationship Management | Marketing Strategy | Product Marketing and Branding | Integrated Marketing | Customer Relationship Management Operations | Market Research | Competitive Business Strategy | Product Management | Market Entry Strategy Formulation | Business Innovation | Business Negotiation | Pricing Strategy | Customer Service Delivery | Financial Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | keep | Business market strategy formulation is explicitly covered. |
| Marketing Management | Manage organisation's marketing plans | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Business-to-Business Customer Relationship Management | Manage relationships with stakeholders for account management, retention and business development purposes | keep | The module description directly supports this skill through busines, customer, relationship. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module description directly supports this skill through market. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | manual review | The module suggests some coverage through market, product, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | keep | The module has direct support for this skill through market. |
| Customer Relationship Management Operations | Manage and analyse customer data to foster long-term relationships with customers and drive sales growth | keep | The module description directly supports this skill through customer, relationship. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module has direct support for this skill through market. |
| Competitive Business Strategy | formulate and implement competitive business development strategies in the organisation | keep | Competitor analysis and business-market strategy formulation are explicit module topics. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Market Entry Strategy Formulation | Develop strategic plans to enter identified markets based on assessed costs, benefits and risks involved | keep | The module description directly supports this skill through formulation, market. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Business Negotiation | Conduct negotiations to establish win-win outcomes for the organisation | keep | Customer negotiations are explicitly listed topics. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Customer Service Delivery | Anticipate customer needs and provide quality customer services as ambassadors of the airports | remove | The taxonomy entry is airport-service specific and unsupported. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Marketing Strategy Development`, `Marketing Management`, `Business-to-Business Customer Relationship Management`, `Marketing Strategy`, `Integrated Marketing`, `Customer Relationship Management Operations`, `Market Research`, `Competitive Business Strategy`, `Product Management`, `Market Entry Strategy Formulation`, `Business Negotiation`, `Pricing Strategy`

Manual review skills: `Product Marketing and Branding`, `Business Innovation`, `Financial Analysis`

## MKT3720 Retail Marketing

Original extracted skills:
```text
Retail Administration | Retailing and the Economy | Retail Space Utilisation | Visual Merchandising Presentation | Point-Of-Purchase Marketing | Store Facilities and Housekeeping | Pricing Strategy | Consumer Intelligence Analysis | Business Innovation | Enterprise Architecture
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Retail Administration | Manage and validate petty cash transactions, as well as document hours worked for each employee | remove | The taxonomy description is specific to HR/talent, which is not reflected in the module. |
| Retailing and the Economy | Anticipate and recognise shifts in the retail landscape, and demonstrate knowledge of the industry context within which the organisational operates in | manual review | The module suggests some coverage through retail, but it does not fully confirm the full taxonomy definition. |
| Retail Space Utilisation | Conceptualise and develop store and digital planograms which illustrate assortment of merchandise | manual review | The module suggests some coverage through retail, but it does not fully confirm the full taxonomy definition. |
| Visual Merchandising Presentation | Monitor accuracy of displays against visual merchandising display guidelines | keep | The module has direct support for this skill through merchandis, visual. |
| Point-Of-Purchase Marketing | Formulate in-store optimal offer strategies design optimal offer assortments and establish Point-of-Purchase (POP) set-up guidelines and promotion per POP to improve sales closures | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Store Facilities and Housekeeping | Identify facility and space requirements and negotiate contract terms and conditions to support business needs and volume | remove | The module title/description centers on `Retail Marketing` rather than `Store Facilities and Housekeeping` as defined in the taxonomy. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Consumer Intelligence Analysis | Devise frameworks for consumer intelligence analysis to develop an understanding of customer knowledge from various customer touch points, for example, customer relationship management (CRM), point-of-sale (POS) an e-commerce systems | remove | The module title/description centers on `Retail Marketing` rather than `Consumer Intelligence Analysis` as defined in the taxonomy. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | remove | Retail strategy and store management are much narrower than enterprise architecture. |

Proposed cleaned skills: `Visual Merchandising Presentation`, `Pricing Strategy`

Manual review skills: `Retailing and the Economy`, `Retail Space Utilisation`, `Point-Of-Purchase Marketing`, `Business Innovation`

## MKT3722 Research for Marketing Insights

Original extracted skills:
```text
Market Research | Market Research and Analysis | Research Design | Marketing Strategy | Integrated Marketing | Product Marketing and Branding | Business Data Analysis | Product Development | Data Collection and Analysis | Qualitative Research | Data Analysis and Interpretation | Report Writing | Arts Education Research
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module description directly supports this skill through market. |
| Market Research and Analysis | Develop market analysis frameworks and objectives to guide and conduct analyses of market trends, developments, competitive factors and economic changes to identify useful business insights, drive economic decisions and forecast market needs | keep | The module description directly supports this skill through analysi, market. |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | keep | The module has direct support for this skill through market, product. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Product Development | Evaluate consumer and market trends to determine value proposition, cost-effectiveness and profitability of proposed products in different markets | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | keep | The module description directly supports this skill through analysi, collection. |
| Qualitative Research | Conduct and lead qualitative research studies, focusing on the study of people, habits, norms and cultures, to uncover insights driving the behaviour of different respondents | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module has direct support for this skill through analysi. |
| Report Writing | Present specific information and evidence in a clear and structured format | keep | Report presentation and writing are explicit learning outcomes. |
| Arts Education Research | Investigate a research focus and hypothesis leading to the generation of insights on current developments, trends and innovative methods of learning delivery and programme design. | remove | This is marketing research, not arts-education research. |

Proposed cleaned skills: `Market Research`, `Market Research and Analysis`, `Research Design`, `Product Marketing and Branding`, `Product Development`, `Data Collection and Analysis`, `Data Analysis and Interpretation`, `Report Writing`

Manual review skills: `Marketing Strategy`, `Integrated Marketing`, `Business Data Analysis`, `Qualitative Research`

## MKT3811 Marketing Analysis & Decision Making

Original extracted skills:
```text
Marketing Strategy | Market Research | Marketing Strategy Development | Product Marketing and Branding | Market Research and Analysis | Marketing Operations Management | Integrated Marketing | Cost Management | Customer Acquisition Management | Financial Analysis | New Product Introduction | Sales Target Management | Project Plan | Data Analysis and Interpretation | Software Design
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | keep | The module has direct support for this skill through market. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | The module description directly supports this skill through market. |
| Marketing Strategy Development | Perform market research to determine the ideal marketing strategy and positioning of retail products | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to retail/merchandising than the module makes clear. |
| Product Marketing and Branding | Develop and implement product marketing strategies by leading sales data collection, segmentation, market research, product marketing idea development and optimisation. Implement product marketing strategies and recommend changes based on desired product and/or corporate positioning and branding | keep | The module description directly supports this skill through brand, market, product. |
| Market Research and Analysis | Develop market analysis frameworks and objectives to guide and conduct analyses of market trends, developments, competitive factors and economic changes to identify useful business insights, drive economic decisions and forecast market needs | keep | The module description directly supports this skill through analysi, market. |
| Marketing Operations Management | Execute marketing tasks and activity operations | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Integrated Marketing | Develop and execute marketing plan on and across various channels and platforms, as well as track customers' responses to and effectiveness of marketing communications on these channels. This also includes the integration of traditional and digital marketing channels and techniques where applicable | manual review | The module suggests some coverage through market, but it does not fully confirm the full taxonomy definition. |
| Cost Management | Analyse, plan and manage costs for cost efficiency and expense reduction | keep | The module has direct support for this skill through cost. |
| Customer Acquisition Management | Develop customer acquisition strategies as well as foster customer relationships to attract new customers | manual review | The module suggests some coverage through customer, but it does not fully confirm the full taxonomy definition. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| New Product Introduction | Support new production by validating build plan to achieve cost-effective production and assembly as well as meeting design specifications | keep | The module has direct support for this skill through product. |
| Sales Target Management | Evaluate and monitor sales target and performance to plan and initiate actions to achieve excellence in sales delivery | manual review | The module suggests some coverage through target, but it does not fully confirm the full taxonomy definition. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | manual review | The module suggests some coverage through plan, but it does not fully confirm the full taxonomy definition. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | The module has direct support for this skill through analysi. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | remove | Spreadsheets and simulations support decisions, but this is not software design. |

Proposed cleaned skills: `Marketing Strategy`, `Market Research`, `Product Marketing and Branding`, `Market Research and Analysis`, `Cost Management`, `New Product Introduction`, `Data Analysis and Interpretation`

Manual review skills: `Marketing Strategy Development`, `Marketing Operations Management`, `Integrated Marketing`, `Customer Acquisition Management`, `Financial Analysis`, `Sales Target Management`, `Project Plan`

## MNO3321 Training and Development

Original extracted skills:
```text
Learning and Development Strategy | Staff Training Facilitation | Human Resource Advisory | Practice Evaluation | Team Effectiveness Management | Organisational Resource Management | Business Presentation Delivery | Lesson Planning | Design Creation and Development | Applications Development
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Learning and Development Strategy | Drive a learning and development culture with strategies to build the organisation's workforce capability | keep | The module has direct support for this skill through learn. |
| Staff Training Facilitation | Identify training needs and develop training roadmaps to improve employees' skills and capabilities. Coordinate staff training and evaluate effectiveness of programmes | manual review | The module suggests some coverage through train, but it does not fully confirm the full taxonomy definition. |
| Human Resource Advisory | Deliver human resource (HR) advisory and consultancy services to internal and external clients to meet their requirements | keep | The module has direct support for this skill through human, resource. |
| Practice Evaluation | Evaluate current and emerging psychological services and initiatives for improvements, adaptions or adoption to advance professional practice | remove | The module title/description centers on `Training and Development` rather than `Practice Evaluation` as defined in the taxonomy. |
| Team Effectiveness Management | Set goals with team and evaluate team effectiveness in achieving the defined goals and objectives | remove | The module title/description centers on `Training and Development` rather than `Team Effectiveness Management` as defined in the taxonomy. |
| Organisational Resource Management | Implement resource management plans which include defining the organisation's resource requirements, functional roles, job role descriptions, reporting lines, accountabilities and responsibilities | keep | The module has direct support for this skill through resource. |
| Business Presentation Delivery | Perform required tasks to prepare and present information in various business settings involving preparation, understanding of audience, delivery and tailoring of messages to be conveyed | manual review | The module suggests some coverage through presentation, but it does not fully confirm the full taxonomy definition. |
| Lesson Planning | Prepare class materials, facilitation approach, and relevant content and activities from the curriculum, including digital aids, in advance of lesson to ensure effective delivery and instruction. | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to education/pedagogy than the module makes clear. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | Training and development modules do not teach software application development. |

Proposed cleaned skills: `Learning and Development Strategy`, `Human Resource Advisory`, `Organisational Resource Management`

Manual review skills: `Staff Training Facilitation`, `Business Presentation Delivery`, `Lesson Planning`, `Design Creation and Development`

## MNO3712 Training and Development

Original extracted skills:
```text
Learning and Development Strategy | Staff Training Facilitation | Human Resource Advisory | Practice Evaluation | Team Effectiveness Management | Organisational Resource Management | Business Presentation Delivery | Lesson Planning | Design Creation and Development | Applications Development
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Learning and Development Strategy | Drive a learning and development culture with strategies to build the organisation's workforce capability | keep | The module has direct support for this skill through learn. |
| Staff Training Facilitation | Identify training needs and develop training roadmaps to improve employees' skills and capabilities. Coordinate staff training and evaluate effectiveness of programmes | manual review | The module suggests some coverage through train, but it does not fully confirm the full taxonomy definition. |
| Human Resource Advisory | Deliver human resource (HR) advisory and consultancy services to internal and external clients to meet their requirements | keep | The module has direct support for this skill through human, resource. |
| Practice Evaluation | Evaluate current and emerging psychological services and initiatives for improvements, adaptions or adoption to advance professional practice | remove | The module title/description centers on `Training and Development` rather than `Practice Evaluation` as defined in the taxonomy. |
| Team Effectiveness Management | Set goals with team and evaluate team effectiveness in achieving the defined goals and objectives | remove | The module title/description centers on `Training and Development` rather than `Team Effectiveness Management` as defined in the taxonomy. |
| Organisational Resource Management | Implement resource management plans which include defining the organisation's resource requirements, functional roles, job role descriptions, reporting lines, accountabilities and responsibilities | keep | The module has direct support for this skill through resource. |
| Business Presentation Delivery | Perform required tasks to prepare and present information in various business settings involving preparation, understanding of audience, delivery and tailoring of messages to be conveyed | manual review | The module suggests some coverage through presentation, but it does not fully confirm the full taxonomy definition. |
| Lesson Planning | Prepare class materials, facilitation approach, and relevant content and activities from the curriculum, including digital aids, in advance of lesson to ensure effective delivery and instruction. | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to education/pedagogy than the module makes clear. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | Training and development modules do not teach software application development. |

Proposed cleaned skills: `Learning and Development Strategy`, `Human Resource Advisory`, `Organisational Resource Management`

Manual review skills: `Staff Training Facilitation`, `Business Presentation Delivery`, `Lesson Planning`, `Design Creation and Development`

## NM3232 Strategic Communication

Original extracted skills:
```text
Strategy Development | Strategy Development and Implementation Management | Marketing Strategy | Media Strategy Development | Research Design | Inbound Marketing | Learning Needs Analysis | Applied Research and Development Management | Design Creation and Development | Scenario Planning and Analysis
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Strategy Development | Develop organisational strategies and policies by analysing the impact of internal and external influencing factors | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Strategy Development and Implementation Management | Develop and implement organisational strategic plans and provide direction to the organisation | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Marketing Strategy | Define an organisational marketing strategy, consider critical industry trends, customer segments and market developments as well as the communication and implementation of the strategy | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Media Strategy Development | Develop, execute and evaluate media strategies and plans to assess impact of media advertising across channels in relation to target customers | keep | The module has direct support for this skill through media. |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Inbound Marketing | Promote organisation's products and services through creating quality, customer-centric content for blogs, podcasts, videos, eBooks, newsletters, whitepapers, SEO, physical products, social media marketing, and other forms of content marketing to attract customers through the different stages of the purchase funnel | remove | The module title/description centers on `Strategic Communication` rather than `Inbound Marketing` as defined in the taxonomy. |
| Learning Needs Analysis | Identify the learning needs of the learners' workplace, department or division in accordance to the Learning Needs Analysis Framework | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to education/pedagogy than the module makes clear. |
| Applied Research and Development Management | Manage research and development projects and activities to innovate and develop new products or operational processes. | manual review | The module suggests some coverage through appli, but it does not fully confirm the full taxonomy definition. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | remove | The module title/description centers on `Strategic Communication` rather than `Design Creation and Development` as defined in the taxonomy. |
| Scenario Planning and Analysis | Define problem statements and analyse data to simulate impact to business operations and propose suitable follow-up actions to sustain operations and achieve business objectives | manual review | The module suggests some coverage through analysi, plann, but it does not fully confirm the full taxonomy definition. |

Proposed cleaned skills: `Media Strategy Development`

Manual review skills: `Strategy Development`, `Strategy Development and Implementation Management`, `Marketing Strategy`, `Research Design`, `Learning Needs Analysis`, `Applied Research and Development Management`, `Scenario Planning and Analysis`

## NM4102 Advanced Communications & New Media Research

Original extracted skills:
```text
Research Design | Data Collection and Analysis | Quantitative Research | Business Data Analysis | Research Proposal Development | Qualitative Analysis | Arts Education Research | Group Work Evaluation | Design Writing | Content Strategy
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | manual review | The module suggests some coverage through analysi, collection, but it does not fully confirm the full taxonomy definition. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Research Proposal Development | Develop research questions, proposals and study protocols | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Qualitative Analysis | Formulate research questions and hypotheses, identify qualitative data sources for analysis of securities and provide investment recommendations based on analysis | keep | The module has direct support for this skill through analysi. |
| Arts Education Research | Investigate a research focus and hypothesis leading to the generation of insights on current developments, trends and innovative methods of learning delivery and programme design. | remove | Communications research methods are not arts-education research. |
| Group Work Evaluation | Evaluate group work processes and specialised intervention strategies for quality and effectiveness of outcomes | manual review | The module suggests some coverage through group, but it does not fully confirm the full taxonomy definition. |
| Design Writing | Convey a design story, idea or concept in a compelling and engaging manner through writing | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Content Strategy | Develop a content strategy to include the conceptualisation and mapping of digital storyboards as well as the optimisation of content delivery parameters to market the organisation's products and services | remove | The module teaches empirical research methods and content analysis, not content-delivery strategy. |

Proposed cleaned skills: `Qualitative Analysis`

Manual review skills: `Research Design`, `Data Collection and Analysis`, `Quantitative Research`, `Business Data Analysis`, `Research Proposal Development`, `Group Work Evaluation`, `Design Writing`

## NM4102HM Advanced Communications & New Media Research

Original extracted skills:
```text
Research Design | Data Collection and Analysis | Quantitative Research | Business Data Analysis | Research Proposal Development | Qualitative Analysis | Arts Education Research | Group Work Evaluation | Design Writing | Content Strategy
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Research Design | Evaluate existing research literature to understand the existing body of knowledge, identify gaps or issues, translate them into research questions and design research studies to investigate and test hypotheses. | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | manual review | The module suggests some coverage through analysi, collection, but it does not fully confirm the full taxonomy definition. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Research Proposal Development | Develop research questions, proposals and study protocols | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Qualitative Analysis | Formulate research questions and hypotheses, identify qualitative data sources for analysis of securities and provide investment recommendations based on analysis | keep | The module has direct support for this skill through analysi. |
| Arts Education Research | Investigate a research focus and hypothesis leading to the generation of insights on current developments, trends and innovative methods of learning delivery and programme design. | remove | Communications research methods are not arts-education research. |
| Group Work Evaluation | Evaluate group work processes and specialised intervention strategies for quality and effectiveness of outcomes | manual review | The module suggests some coverage through group, but it does not fully confirm the full taxonomy definition. |
| Design Writing | Convey a design story, idea or concept in a compelling and engaging manner through writing | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Content Strategy | Develop a content strategy to include the conceptualisation and mapping of digital storyboards as well as the optimisation of content delivery parameters to market the organisation's products and services | remove | The module teaches empirical research methods and content analysis, not content-delivery strategy. |

Proposed cleaned skills: `Qualitative Analysis`

Manual review skills: `Research Design`, `Data Collection and Analysis`, `Quantitative Research`, `Business Data Analysis`, `Research Proposal Development`, `Group Work Evaluation`, `Design Writing`

## PF2109 Project Feasibility

Original extracted skills:
```text
Project Plan | Project Feasibility Assessment | Design Creation and Development | Property Operations Management | Site Assessment and Analysis | Project Integration | Infrastructure Strategy | Cost Management | Project Cost | Applications Development | Market Research
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Project Feasibility Assessment | Study project feasibility to meet project outcomes and objectives | keep | The module has direct support for this skill through feasibility. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Property Operations Management | Manage property operations and evaluate operational results to ensure operational efficiency and high service standards to enhance guest experience | remove | The module title/description centers on `Project Feasibility` rather than `Property Operations Management` as defined in the taxonomy. |
| Site Assessment and Analysis | Plan and execute assessments of project sites to evaluate suitability for built environment operations | remove | The taxonomy description is specific to construction/BIM, which is not reflected in the module. |
| Project Integration | Set programme direction as well as balance overall project management functions across the project life cycle | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Infrastructure Strategy | Develop a robust strategy and plan for defining and managing a future-ready IT infrastructure, optimising its capacity, availability and synchronisation to enable an organisation's business operations. This involves evaluating infrastructure models and options for infrastructure components, managing infrastructure investments and facilitating the transformation toward the desired future infrastructure model | remove | Project feasibility is not IT infrastructure planning. |
| Cost Management | Analyse, plan and manage costs for cost efficiency and expense reduction | manual review | The module suggests some coverage through cost, but it does not fully confirm the full taxonomy definition. |
| Project Cost | Set budgets, monitor costs and assess budget implications of projects on operations | keep | The module description directly supports this skill through cost. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | Feasibility, site study, and project brief work do not imply app development. |
| Market Research | formulate market research frameworks, as well as develop market research study objectives, market research plans and methodologies to analyse market trends and developments to forecast emerging market needs | keep | Market study is explicitly part of project-feasibility work. |

Proposed cleaned skills: `Project Feasibility Assessment`, `Project Cost`, `Market Research`

Manual review skills: `Project Plan`, `Design Creation and Development`, `Project Integration`, `Cost Management`

## PF3305 Facilities Planning and Design

Original extracted skills:
```text
Facility Design | Facility Maintenance | Confined Space Management | Site Assessment and Analysis | Project Plan | Design Creation and Development | Learning Environment Design | Environmental Protection Management | Visioning and Strategic Planning | Design Concepts Generation | Capital Management | Human Factors in Job Design
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Facility Design | Design and integrate biopharmaceuticals manufacturing facilities to optimise operational efficiency and effectiveness | manual review | Facility design is relevant, but the matched taxonomy entry is specifically about biopharma facilities. |
| Facility Maintenance | Manage facility system maintenance activities to manufacturing and business operations | manual review | The module suggests some coverage through facility, but it does not fully confirm the full taxonomy definition. |
| Confined Space Management | Assess safety when working in confined spaces under the relevant regulations | remove | The module is about facilities planning and design rather than confined-space safety. |
| Site Assessment and Analysis | Plan and execute assessments of project sites to evaluate suitability for built environment operations | keep | Site analysis is explicitly named in the module description. |
| Project Plan | Develop project plans and manage project risks using appropriate project management tools | manual review | The module suggests some coverage through plan, but it does not fully confirm the full taxonomy definition. |
| Design Creation and Development | Utilise relevant design approaches for the conceptualisation, development and enhancement of design solutions | remove | The module title/description centers on `Facilities Planning and Design` rather than `Design Creation and Development` as defined in the taxonomy. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | The module is general facilities planning/design, not pedagogy-focused learning-environment design. |
| Environmental Protection Management | Establish policies and procedures for sustainable environment practices covering green procurement, gas emissions, disposal methods, product quality standards and regulatory compliance | manual review | The module suggests some coverage through environmental, but it does not fully confirm the full taxonomy definition. |
| Visioning and Strategic Planning | Foster shared vision and mission among educators and guide them to ensure alignment of their daily work to the Centre's long-term objectives | remove | The taxonomy entry is educator/centre-management specific, not facilities planning. |
| Design Concepts Generation | Build preliminary ideas on innovative design concepts and different ways to address needs and opportunities of target stakeholders | remove | The module title/description centers on `Facilities Planning and Design` rather than `Design Concepts Generation` as defined in the taxonomy. |
| Capital Management | Calculate capital adequacy ratios to determine capital buffers necessary for the bank or financial institution, while optimising returns on capital based on capital allocation strategies | remove | Capital planning here is facilities planning, not bank capital adequacy or buffers. |
| Human Factors in Job Design | Identify and mitigate risks of incidents and/or accidents caused by human factors | keep | The module description directly supports this skill through factor, human. |

Proposed cleaned skills: `Site Assessment and Analysis`, `Human Factors in Job Design`

Manual review skills: `Facility Design`, `Facility Maintenance`, `Project Plan`, `Environmental Protection Management`

## PL4245 Data Science for Psychology: Methods and Applications

Original extracted skills:
```text
Learning Analytics | Programming and Coding | Business Data Analysis | Data Visualisation | Artificial Intelligence Application | Quantitative Research | Data and Statistical Analytics | Trend Forecasting | Data-Mining and Modelling | Mathematical Concepts Application
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Learning Analytics | Analyse data to glean insights and drive decision making to enhance learning delivery, in accordance with governance and management policies for the handling of data at various stages of its lifecycle. | manual review | The module suggests some coverage through learn, but it does not fully confirm the full taxonomy definition. |
| Programming and Coding | Produce the technology required for a visual effects (VFX) project | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to games/VFX/media than the module makes clear. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | keep | The module description directly supports this skill through artificial, intelligence. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | remove | The module title/description centers on `Data Science for Psychology: Methods and Applications` rather than `Quantitative Research` as defined in the taxonomy. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | keep | The module has direct support for this skill through statistical. |
| Trend Forecasting | Drive the practice of collecting and comparing information over time to identify trends and patterns, in order to predict and plan for future events | remove | The module title/description centers on `Data Science for Psychology: Methods and Applications` rather than `Trend Forecasting` as defined in the taxonomy. |
| Data-Mining and Modelling | Establish and deploy data modelling techniques to support narrative and predictive analytics efforts and identify trends and patterns for simulation and forecasting purposes | manual review | The module suggests some coverage through min, but it does not fully confirm the full taxonomy definition. |
| Mathematical Concepts Application | Apply mathematical concepts to solve engineering problems | remove | The module title/description centers on `Data Science for Psychology: Methods and Applications` rather than `Mathematical Concepts Application` as defined in the taxonomy. |

Proposed cleaned skills: `Artificial Intelligence Application`, `Data and Statistical Analytics`

Manual review skills: `Learning Analytics`, `Programming and Coding`, `Business Data Analysis`, `Data Visualisation`, `Data-Mining and Modelling`

## PL4245HM Data Science for Psychology: Methods and Applications

Original extracted skills:
```text
Learning Analytics | Programming and Coding | Business Data Analysis | Data Visualisation | Artificial Intelligence Application | Quantitative Research | Data and Statistical Analytics | Trend Forecasting | Data-Mining and Modelling | Mathematical Concepts Application
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Learning Analytics | Analyse data to glean insights and drive decision making to enhance learning delivery, in accordance with governance and management policies for the handling of data at various stages of its lifecycle. | manual review | The module suggests some coverage through learn, but it does not fully confirm the full taxonomy definition. |
| Programming and Coding | Produce the technology required for a visual effects (VFX) project | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to games/VFX/media than the module makes clear. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Artificial Intelligence Application | Apply algorithmic, statistical and engineering knowledge to integrate artificial intelligence into engineering processes | keep | The module description directly supports this skill through artificial, intelligence. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | remove | The module title/description centers on `Data Science for Psychology: Methods and Applications` rather than `Quantitative Research` as defined in the taxonomy. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | keep | The module has direct support for this skill through statistical. |
| Trend Forecasting | Drive the practice of collecting and comparing information over time to identify trends and patterns, in order to predict and plan for future events | remove | The module title/description centers on `Data Science for Psychology: Methods and Applications` rather than `Trend Forecasting` as defined in the taxonomy. |
| Data-Mining and Modelling | Establish and deploy data modelling techniques to support narrative and predictive analytics efforts and identify trends and patterns for simulation and forecasting purposes | manual review | The module suggests some coverage through min, but it does not fully confirm the full taxonomy definition. |
| Mathematical Concepts Application | Apply mathematical concepts to solve engineering problems | remove | The module title/description centers on `Data Science for Psychology: Methods and Applications` rather than `Mathematical Concepts Application` as defined in the taxonomy. |

Proposed cleaned skills: `Artificial Intelligence Application`, `Data and Statistical Analytics`

Manual review skills: `Learning Analytics`, `Programming and Coding`, `Business Data Analysis`, `Data Visualisation`, `Data-Mining and Modelling`

## QF3101 Investment Instruments and Risk Management

Original extracted skills:
```text
Hedging Management | Financial Analysis | Financial Modelling | Market Risk Management | Risk Management | Pricing Strategy | Risk Assessment | Value Analysis | Derivatives Trading Management | Trading Management | Contract Management
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Hedging Management | Execute hedging strategies to mitigate risks arising from fuel and foreign exchange (FOREX) volatilities | keep | The module description directly supports this skill through hedg. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | keep | The module description directly supports this skill through analysi, finance. |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | manual review | The module suggests some coverage through finance, but it does not fully confirm the full taxonomy definition. |
| Market Risk Management | Identify, monitor, and manage market risks including foreign exchange, interest rates, credit spreads, and liquidity, and implement risk mitigation plans in adherence to financial market risk limits and guidelines. | keep | The module description directly supports this skill through market, risk. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Pricing Strategy | Analyse product, organisational and market factors, trends, pricing scenarios and valuation models to develop effective pricing strategies for products and solutions | keep | The module description directly supports this skill through pric. |
| Risk Assessment | Perform assessment of risks, including fraud risks, through understanding the client's business | manual review | The module suggests some coverage through risk, but it does not fully confirm the full taxonomy definition. |
| Value Analysis | Establish the organisational value stream, enhance value-add and reduce costs | manual review | The module suggests some coverage through analysi, value, but it does not fully confirm the full taxonomy definition. |
| Derivatives Trading Management | Perform structured trades for proprietary and risk management objectives by identifying market-making opportunities | keep | The module description directly supports this skill through derivativ, trad. |
| Trading Management | Perform trades and take positions in various products in accordance with trading plans | manual review | The module suggests some coverage through trad, but it does not fully confirm the full taxonomy definition. |
| Contract Management | Manage contract creation, execution and analysis to maximise financial and operational performance and minimise risks | keep | The module description directly supports this skill through contract. |

Proposed cleaned skills: `Hedging Management`, `Financial Analysis`, `Market Risk Management`, `Risk Management`, `Pricing Strategy`, `Derivatives Trading Management`, `Contract Management`

Manual review skills: `Financial Modelling`, `Risk Assessment`, `Value Analysis`, `Trading Management`

## QF4212 Data Science in FinTech

Original extracted skills:
```text
Financial Modelling | Financial Analysis | Derivatives Trading Management | Risk Management | Data Engineering | Portfolio Management | Business Data Analysis | Data and Statistical Analytics | Analytics and Computational Modelling | Financial Transactions | Data Visualisation | Big Data Analytics
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Financial Modelling | Develop financial models and valuation models to arrive at a valuation conclusion | keep | The module description directly supports this skill through finance. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | keep | The module description directly supports this skill through analysi, finance. |
| Derivatives Trading Management | Perform structured trades for proprietary and risk management objectives by identifying market-making opportunities | keep | The module has direct support for this skill through derivativ. |
| Risk Management | Apply organisational policies and procedures to manage and control financial and non-financial risks | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Data Engineering | Develop and implement efficient and stable processes to collect, store, extract, transform, load and integrate data at various stages in the data pipeline. This also involves processing varying amounts of data from a variety of sources and preparing data in a structure that is easily access and analysed according to business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Portfolio Management | Manage systematically the IT investments, projects, services and activities within a company, in line with business objectives and priorities. This involves the development of a framework to evaluate potential costs and benefits and make key decisions about IT investments, internal allocation and utilisation of IT resources and/or assets and any changes to IT processes or services offered | remove | The taxonomy definition is about IT portfolio governance, not finance portfolios. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The module suggests some coverage through statistical, but it does not fully confirm the full taxonomy definition. |
| Analytics and Computational Modelling | Develop, select and apply algorithms and advanced computational methods to enable systems or software agents to learn, improve, adapt and produce desired outcomes or tasks which also involves the interpretation of data, including the application of data modelling techniques to explore and address a specific issue or requirement | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Financial Transactions | Prepare business documentation and cash balances | remove | The module models financial data but does not teach transaction processing. |
| Data Visualisation | Implement contemporary techniques, dynamic visual displays with illustrative and interactive graphics to present patterns, trends, analytical insights from data or new concepts in a strategic manner for the intended audience | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Big Data Analytics | Apply data extraction and analytic methods to analyse and evaluate financial and non-financial information and provide business intelligence | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Financial Modelling`, `Financial Analysis`, `Derivatives Trading Management`, `Risk Management`

Manual review skills: `Data Engineering`, `Business Data Analysis`, `Data and Statistical Analytics`, `Analytics and Computational Modelling`, `Data Visualisation`, `Big Data Analytics`

## RE1707 Real Estate, Society and Enterprise

Original extracted skills:
```text
Property Operations Management | Financial Analysis | Business Needs Analysis | Strategy Planning | Business Innovation | Architecture Design | Building Information Modelling Application | Enterprise Architecture | Asset Management | Sustainable Investment Management | Community Development | Technology Assessment
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Property Operations Management | Manage property operations and evaluate operational results to ensure operational efficiency and high service standards to enhance guest experience | manual review | The module suggests some coverage through property, but it does not fully confirm the full taxonomy definition. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | Real-estate finance and investment are covered, but financial-statement analysis is not explicit. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | manual review | Market and enterprise analysis are relevant, but formal business-requirements analysis is broader than the module. |
| Strategy Planning | Develop organisational strategies and policies by analysing the impact of internal and external influencing factors and seeking consultation from relevant stakeholders. | keep | Strategic planning and urban/real-estate planning are explicitly covered. |
| Business Innovation | Identify and evaluate digitisation and innovative business opportunities provided by new advancements in information and communication technology to establish new services or businesses to bridge the physical and digital worlds | manual review | The module suggests some coverage through busines, but it does not fully confirm the full taxonomy definition. |
| Architecture Design | Utilise holistic design approaches for the conceptualisation, development and enhancement of design solutions | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Building Information Modelling Application | Use Building information Modelling to make design, project and operational information accurate, accessible and actionable | manual review | The module suggests some coverage through build, but it does not fully confirm the full taxonomy definition. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | remove | The module is about real estate and cities, not enterprise-architecture planning. |
| Asset Management | Formulate and implement the organisation's asset management policies to optimise asset life-cycles and performance. | keep | Asset enhancement and real-estate investment directly support asset management. |
| Sustainable Investment Management | Lead organisation's strategies on sustainable investment and implement sustainable investment concepts and approaches on portfolio management | keep | The module has direct support for this skill through investment. |
| Community Development | Build, grow and manage community relationships across a variety of online and offline platforms to generate brand awareness, understand customers' needs, increase customer engagement and develop customer loyalty | keep | The module description directly supports this skill through community. |
| Technology Assessment | Evaluate patentability and commercial value of technical disclosures | remove | The module discusses property technology, but not patentability or technical-disclosure assessment. |

Proposed cleaned skills: `Strategy Planning`, `Asset Management`, `Sustainable Investment Management`, `Community Development`

Manual review skills: `Property Operations Management`, `Financial Analysis`, `Business Needs Analysis`, `Business Innovation`, `Architecture Design`, `Building Information Modelling Application`

## RE2707 Asset and Property Management

Original extracted skills:
```text
Facility Maintenance | Property Operations Management | Building Management System Implementation and Control | Asset and Liability Management | Fire Prevention and Firefighting | Maintenance Coordination | Confined Space Management | Sustainable Investment Management | Learning Environment Design | Enterprise Architecture
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Facility Maintenance | Manage facility system maintenance activities to manufacturing and business operations | keep | The module description directly supports this skill through facility, maintenance. |
| Property Operations Management | Manage property operations and evaluate operational results to ensure operational efficiency and high service standards to enhance guest experience | manual review | The module suggests some coverage through property, but it does not fully confirm the full taxonomy definition. |
| Building Management System Implementation and Control | Implement Building Management System (BMS) to integrate overall building systems to improve the efficiency and productivity of management | manual review | The module suggests some coverage through build, but it does not fully confirm the full taxonomy definition. |
| Asset and Liability Management | Address risks faced by financial institutions or banks due to mismatch between assets and liabilities by performing capital, liquidity, interest rate and balance sheet management. | manual review | The module suggests some coverage through asset, but it does not fully confirm the full taxonomy definition. |
| Fire Prevention and Firefighting | Minimise the risk of fire in civil aviation situations and maintain operational readiness to respond to emergency situations involving structural fires | manual review | The module suggests some coverage through fire, but it does not fully confirm the full taxonomy definition. |
| Maintenance Coordination | Establish and implement organisational maintenance strategies and programmes | manual review | The module suggests some coverage through maintenance, but it does not fully confirm the full taxonomy definition. |
| Confined Space Management | Assess safety when working in confined spaces under the relevant regulations | manual review | The module suggests some coverage through space, but it does not fully confirm the full taxonomy definition. |
| Sustainable Investment Management | Lead organisation's strategies on sustainable investment and implement sustainable investment concepts and approaches on portfolio management | keep | The module has direct support for this skill through investment. |
| Learning Environment Design | Create high-quality learning environments across digital, physical, and hybrid spaces that promote the achievement of desired learning outcomes conducive to the specific art form and pedagogy, including classroom format, use of technology, interior design, and learner demographic and learner style considerations. | remove | Property management does not support pedagogy-oriented learning-space design. |
| Enterprise Architecture | Operationalise a business strategy on the planning and development of business structures and models to facilitate the evolution of a business to its desired future state. This involves the review and prioritisation of market trends, evaluation of alternative strategies, as well as the strategic evaluation and utilisation of enterprise capability and technology to support business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Facility Maintenance`, `Sustainable Investment Management`

Manual review skills: `Property Operations Management`, `Building Management System Implementation and Control`, `Asset and Liability Management`, `Fire Prevention and Firefighting`, `Maintenance Coordination`, `Confined Space Management`, `Enterprise Architecture`

## RE3807 Corporate Finance for Real Estate

Original extracted skills:
```text
Corporate Governance | Valuation | Financial Analysis | Property Operations Management | Financial Statements Analysis | Capital Management | Business Needs Analysis | Sustainable Investment Management | Trading Analysis | Capital Raising | Financial Statements Review
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Corporate Governance | Develop corporate governance frameworks, establish and implement operationalisation of policies to maintain compliance to statutory laws and regulatory policies | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Valuation | Perform valuation for business and financial assets for deal structuring | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | keep | The module description directly supports this skill through analysi, finance. |
| Property Operations Management | Manage property operations and evaluate operational results to ensure operational efficiency and high service standards to enhance guest experience | remove | Corporate real-estate finance is not guest-facing property operations. |
| Financial Statements Analysis | Analyse financial statements in accordance with the applicable frameworks | keep | The module description directly supports this skill through analysi, finance, statement. |
| Capital Management | Calculate capital adequacy ratios to determine capital buffers necessary for the bank or financial institution, while optimising returns on capital based on capital allocation strategies | manual review | The module suggests some coverage through capital, but it does not fully confirm the full taxonomy definition. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Sustainable Investment Management | Lead organisation's strategies on sustainable investment and implement sustainable investment concepts and approaches on portfolio management | remove | The module title/description centers on `Corporate Finance for Real Estate` rather than `Sustainable Investment Management` as defined in the taxonomy. |
| Trading Analysis | Develop market research reports to support trading strategies | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Capital Raising | Acquire or raise capital and funds to carry out organisational goals and objectives | manual review | The module suggests some coverage through capital, but it does not fully confirm the full taxonomy definition. |
| Financial Statements Review | Review financial statements in accordance with applicable frameworks and regulatory requirements | keep | The module description directly supports this skill through finance, statement. |

Proposed cleaned skills: `Corporate Governance`, `Valuation`, `Financial Analysis`, `Financial Statements Analysis`, `Financial Statements Review`

Manual review skills: `Capital Management`, `Business Needs Analysis`, `Trading Analysis`, `Capital Raising`

## SA4101 Software Analysis and Design

Original extracted skills:
```text
User Interface Design | User Experience Design | Software Design | Agile Software Development | Cloud Computing Application | Internet of Things Application | Applications Development | Engineering Product Design | Product Management | Project Management | Container Operations | Project Integration | Website Design
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| User Interface Design | Design user interfaces for machines and software, incorporating visual, technical and functional elements that facilitate ease of access, understanding and usage. This would involve adding, removing, modifying or enhancing elements to make the user's interaction with the product as seamless as possible | keep | UI design aligns directly with the software analysis and design focus. |
| User Experience Design | Conceptualise and enhance the users' interactions and engagement with products and services by integrating elements of interaction design, information architecture, information design, visual interface design, user assistance design and user-centered design | keep | UX design aligns directly with the module. |
| Software Design | Create and refine the overall plan for the design of software, including the design of functional specifications starting from the defined business requirements as well as the consideration and incorporation of various controls, functionality and interoperability of different elements into a design blueprint or model which describes the overall architecture in hardware, software, databases, and third party frameworks that the software will use or interact with | keep | Software design is directly named by the module title. |
| Agile Software Development | Plan and implement Agile methodology and the use of adaptive and iterative methods and techniques in the software development lifecycle to account for continuous evolution, development, and deployment to enable seamless delivery of the application to the end user | keep | Agile software delivery fits the module context. |
| Cloud Computing Application | Implement cloud solutions to enhance business performance and security of IT systems | keep | The module supports software solution design that can include cloud applications. |
| Internet of Things Application | Interrelate computing devices, equipment and machines data in a networked environment to provide specific solutions | keep | The software-product design context supports IoT application work. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | keep | The module includes designing and building software solutions. |
| Engineering Product Design | Facilitate the design of products to meet requirements for functionality and performance | manual review | Product design is relevant, but the taxonomy entry is more engineering-oriented. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | keep | Software product definition and design strongly support product management. |
| Project Management | Execute projects by managing stakeholder engagement, resources, budgets and resolving problems | keep | The module is project-oriented and supports project-management work. |
| Container Operations | Perform container cargo loading and unloading through the use of quay cranes and coordination between wharves and container yards | remove | The taxonomy entry is shipping/logistics specific and unsupported. |
| Project Integration | Set programme direction as well as balance overall project management functions across the project life cycle | manual review | Project delivery is present, but the taxonomy definition is broader. |
| Website Design | Determine and review purposes, expectations and functionalities of websites, as well as analyse the user-interface design requirements | keep | Website design is directly relevant to software design work. |

Proposed cleaned skills: `User Interface Design`, `User Experience Design`, `Software Design`, `Agile Software Development`, `Cloud Computing Application`, `Internet of Things Application`, `Applications Development`, `Product Management`, `Project Management`, `Website Design`

Manual review skills: `Engineering Product Design`, `Project Integration`

## ST2137 Statistical Computing and Programming

Original extracted skills:
```text
Data and Statistical Analytics | Data Collection and Analysis | Quantitative Research | Data Analysis and Interpretation | Data Design | Business Data Analysis | Programming and Coding | Scriptwriting | Parametric Testing | Control System Programming | Applications Development
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | manual review | The module suggests some coverage through statistical, but it does not fully confirm the full taxonomy definition. |
| Data Collection and Analysis | Collect, extract and interpret data according to defined requirements to obtain project insights | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Data Design | Specify and create a data structure or database model, including the setting of various parameters or fields that can be modified to suit different structured or unstructured data requirements, the design of data flow, as well as the development of mechanisms for maintenance, storage and retrieval of data based on the business requirements | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Data Analysis | Implementing data analytics within the organisation to generate business insights and intelligence through the use of statistical and computational techniques and tools, algorithms, predictive data modelling and data visualisation | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Programming and Coding | Produce the technology required for a visual effects (VFX) project | manual review | The title fits statistical computing, but the taxonomy definition is VFX-specific. |
| Scriptwriting | Create compelling and engaging scripts for media content of different formats on various platforms | remove | The module teaches statistical programming, not writing scripts for media content. |
| Parametric Testing | Implement parametric tests and parametric data analysis to drive process and yield improvements | keep | The module has direct support for this skill through test. |
| Control System Programming | Develop capabilities in areas of communications and remote operations by programming logic circuits and erasable programmable read-only memory for ships, rigs and/or conversions | remove | Statistical programming is not marine/offshore control-system programming. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | remove | The module title/description centers on `Statistical Computing and Programming` rather than `Applications Development` as defined in the taxonomy. |

Proposed cleaned skills: `Parametric Testing`

Manual review skills: `Data and Statistical Analytics`, `Data Collection and Analysis`, `Quantitative Research`, `Data Analysis and Interpretation`, `Data Design`, `Business Data Analysis`, `Programming and Coding`

## ST4243 Statistical Methods for DNA Microarray Analysis

Original extracted skills:
```text
Genetic Knowledge Analysis | Laboratory Data Analysis | Data and Statistical Analytics | Quantitative Research | Data Analysis and Interpretation | Test Planning | Talent Capability Assessment | Research | Financial Analysis | Learning Solution Design | Patient education in genetics
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Genetic Knowledge Analysis | Demonstrate, utilise and integrate genetic and genomic knowledge in practice | keep | The module description directly supports this skill through analysi, genetic, knowledge. |
| Laboratory Data Analysis | Analyse laboratory data | keep | The module has direct support for this skill through analysi. |
| Data and Statistical Analytics | Identify data sets for application of statistical techniques to analyse and interpret large complex data to uncover trends or patterns in order to locate and define new process improvement opportunities | keep | The module description directly supports this skill through statistical. |
| Quantitative Research | Conduct and lead systematic statistical, mathematical and numerical analyses to formulate facts, uncover patterns in research, test hypotheses and draw sound conclusions for problem-solving | keep | The module is heavily quantitative and research-oriented. |
| Data Analysis and Interpretation | Extract meaningful patterns and insights from data to improve organisational performance and decision-making | keep | Interpreting microarray experiment results is central to the module. |
| Test Planning | Develop testing plans and procedures by determining scope and risks, identifying the objects of testing, selecting test methods and tools, and controlling test implementation | manual review | The module suggests some coverage through test, but it does not fully confirm the full taxonomy definition. |
| Talent Capability Assessment | Develop talent assessment processes with assessment tools to evaluate employees' capabilities | remove | The module title/description centers on `Statistical Methods for DNA Microarray Analysis` rather than `Talent Capability Assessment` as defined in the taxonomy. |
| Research | Optimising manufacturing processes, material developments and development of new product line | remove | The module title/description centers on `Statistical Methods for DNA Microarray Analysis` rather than `Research` as defined in the taxonomy. |
| Financial Analysis | Analyse the financial statements and data to provide insights about the financial performance and position of the organisation over time | manual review | The module suggests some coverage through analysi, but it does not fully confirm the full taxonomy definition. |
| Learning Solution Design | Design and evaluate learning solutions which drive performance enhancement | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Patient education in genetics | Communicate with patients and caregivers to deliver and facilitate the continuity of care | remove | This is a statistics course on microarray analysis, not patient or caregiver communication. |

Proposed cleaned skills: `Genetic Knowledge Analysis`, `Laboratory Data Analysis`, `Data and Statistical Analytics`, `Quantitative Research`, `Data Analysis and Interpretation`

Manual review skills: `Test Planning`, `Financial Analysis`, `Learning Solution Design`

## TR3001 New Product Development

Original extracted skills:
```text
Engineering Product Design | Product Development | Design for Manufacturing and Assembly | Product Management | Project Management | Business Needs Analysis | Digital and Physical Prototyping | Product Demonstration | Learning and Development Programme Management | Concept Creation | User Experience Design | Applications Development
```

| Skill | Skill Description | Decision | Rationale |
| --- | --- | --- | --- |
| Engineering Product Design | Facilitate the design of products to meet requirements for functionality and performance | keep | The module has direct support for this skill through product. |
| Product Development | Evaluate consumer and market trends to determine value proposition, cost-effectiveness and profitability of proposed products in different markets | keep | The skill title appears directly in the module text and the taxonomy description is broadly aligned. |
| Design for Manufacturing and Assembly | Apply Design for Manufacturing and Assembly (DfMA) principles throughout construction project lifecycle to ensure effectiveness, safety and economies of scale for manufacturing and assembly | manual review | DfMA topics are relevant, but the taxonomy definition is framed around construction-lifecycle work. |
| Product Management | Create and manage a product roadmap, involving the ideating, planning, forecasting, marketing and management of a product or a suite of products throughout stages of its lifecycle, from its conceptualisation to market entrance and eventual phasing-out. This includes the creation of a new product idea or concept and definition of the product strategy based on a projection of its potential benefits to the customer as well as the review of product performance against milestones and targets set | manual review | The module suggests some coverage through product, but it does not fully confirm the full taxonomy definition. |
| Project Management | Execute projects by managing stakeholder engagement, resources, budgets and resolving problems | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Business Needs Analysis | Identify and scope business requirements and priorities through rigorous information gathering and analysis as well as clarification of the solutions, initiatives and programmes to enable effective delivery. This also involves the development of a compelling and defensible business case and the articulation of the potential impact of the solution to the business | remove | The module title/description centers on `New Product Development` rather than `Business Needs Analysis` as defined in the taxonomy. |
| Digital and Physical Prototyping | Construct design concepts, either digitally or physically, to develop deeper understanding of the designs and test their usability and functionality | manual review | The skill is somewhat plausible, but the taxonomy description is more specific to construction/BIM than the module makes clear. |
| Product Demonstration | Develop knowledge of the range and price of the organisation's products and services, as well as present and demonstrate the use and application of products and services to customers | manual review | The module suggests some coverage through product, but it does not fully confirm the full taxonomy definition. |
| Learning and Development Programme Management | Establish and implement learning and development programmes and channels to facilitate employees' growth and capability building | remove | Product development projects do not cover employee L&D programme management. |
| Concept Creation | Develop the initial concepts or ideas for creation of media products and platforms | keep | The module has direct support for this skill through concept. |
| User Experience Design | Conceptualise and enhance the users' interactions and engagement with products and services by integrating elements of interaction design, information architecture, information design, visual interface design, user assistance design and user-centered design | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |
| Applications Development | Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components | manual review | The match is plausible from the module title or description, but not strong enough to confirm confidently. |

Proposed cleaned skills: `Engineering Product Design`, `Product Development`, `Concept Creation`

Manual review skills: `Design for Manufacturing and Assembly`, `Product Management`, `Project Management`, `Digital and Physical Prototyping`, `Product Demonstration`, `User Experience Design`, `Applications Development`

## Aggregate Summary

- Reviewed modules: 85
- Reviewed exact-match skills: 978
- `keep`: 354
- `manual review`: 455
- `remove`: 169
