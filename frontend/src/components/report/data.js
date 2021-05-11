export const report = [
    {
        section: "Introduction",
        text: "Argumentation can be considered one of the core principles on which human interaction is based. It is an intelligent communication task aiming at increasing or decreasing the acceptability of a controversial claim or point of view (Moens, 2018). Convincing others by bringing up arguments supporting or attacking claims builds the basis of discursive activity which is crucial in legal reasoning. Because human argumentation is expressed in natural language and strongly context-dependent, the ability to conduct contextual discussions was believed to be unique. However, what if machines could be taught to extract arguments from human discourse?"
    },
    {
        section: "Problem - Time is Money",
        text: "Case law plays an important role in legal argumentation and decision-making, especially in countries with legal systems using common law (Milward, Mochales, Moens, & Wyner, 2010). Lawyers need to dig into documents of past judicial decisions (precedents) and identify previous decisions supporting their side in the legal dispute and undermining the other. The analysis of these documents requires skill and a lot of time: Cases are expressed in natural language, consider highly complex matters under dispute, and have complex interrelationships while the number of documents is constantly growing. Moreover, navigating the documents, interpreting, and applying the results successfully needs extensive training. These factors can furthermore lead to extensive costs of legal proceedings because of additional working hours and high fees of lawyers (skill premium)."
    },
    {
        section: "Solution - LAWrgMiner",
        text: "The combination of the fields of Artificial Intelligence (AI) and Natural Language Processing (NLP) offers an instrument to help lawyers manage and search through the existing case law: Argumentation mining. Generally, its goal is to extract claims and premises from text expressed in natural language (Milward, Mochales, Moens, & Wyner, 2010). This is where the LAWrgMiner comes into play. LAWrgMiner, a neural network trained on the ECHR dataset, aims to extract natural language arguments from legal documents. It allows a lawyer to extract arguments from an unstructured legal proceeding and presents them in an easily understandable and structured way. While they normally must invest hours into manually reading through the case law and searching for arguments, LAWrgMiner reduces the time invested from searching for multiple hours to presenting claims and premises within the uploaded source in a couple of minutes. With LAWrgMiner, we make two contributions. First, we train an existing argumentation miner, Targer (Chernodub et al., 2019), on a more specialized dataset than it was trained on until today. Second, we interviewed legal professionals in order to gather user requirements for the tool. Due to the time constraints of the course, we had to prioritize them strictly and focus on showing the proof of concept of an argument miner in the field of law. For example, we implemented a list view of claims and premises extracted from a legal case but moved the integration of an API for case law databases to the future work. "
            },
    {
        section: "The Argument Mining Framework",
        text: "Targer, an open-source system for tagging arguments in free text and for retrieving arguments from web-scale corpora is the base of LAWrgMiner’s argumentation mining model. Targer was chosen due to it being an open-source project, developed and extended to fit a wide range of application areas, which allowed us to train it on the ECHR dataset with only a few modifications. Alternatives like Margot, args.me, or ArgumenText do not offer the possibility to train them from ground up, based on a new dataset."
    },
    {
        section: "References",
        text: [
            "Cabrio, E., & Villata, S. (2018). Five Years of Argument Mining: a Data-driven Analysis. Conference: Twenty-Seventh International Joint Conference on Artificial Intelligence {IJCAI-18}. doi:10.24963/ijcai.2018/766",
            "Chernodub, A., Oliynyk, O., Heidenreich, P., Bondarenko, A., Hagen, M., Biemann, C. & Panchenko, A. (2019). TARGER: Neural Argument Mining at Your Fingertips. Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations, 195-200. doi.org/10.18653/v1/P19-3031.",
            "Ein-Dor, L., Eyal Shnarch, Lena Dankin, Alon Halfon, B. Sznajder, Ariel Gera, Carlos Alzate, Martin Gleize, Leshem Choshen, Yufang Hou, Yonatan Bilu, R. Aharonov & N. Slonim (2020). Corpus Wide Argument Mining - a Working Solution. The Thirty-Fourth AAAI Conference on Artificial Intelligence, 7683-7691.",
            "Milward, D., Mochales, R., Moens, M. & Wyner, A. (2010). Approaches to text mining arguments from legal cases. In E. Francesconi, S. Montemagni, W. Peters, & D. Tiscornia (Eds.), Semantic processing",
            "Lawrence, J. & Reed, C. (2019). Argument Mining: A Survey. Computational Linguistics, 45(4), 765–818. doi:10.1162/coli_a_00364.",
            "Mochales, R. & Moens, M. (2011). Argumentation mining. Artificial Intelligence and Law 19(1), 1-22. doi:10.1007/s10506-010-9104-x",
            "Moens, M. (2018). Argumentation mining: How can a machine acquire common sense and world knowledge? Argument & Computation 9, 1–14. doi:10.3233/AAC-170025",
            "Poudyal, P., Savelka, J., Ieven, A., Moens, M., Gonçalves, T., & Quaresma, P. (2020). ECHR: Legal Corpus for Argument Mining. Proceedings of the 7th Workshop on Argument Mining, 67–75 Barcelona.",
            "Stab, C. & Gurevych, I. (2013). Guidelines for Annotating Argument Components and Relations in Persuasive Essays.",
        ],
    },
];
