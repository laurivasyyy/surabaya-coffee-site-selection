# Notebook Development Standard

The default standard for every notebook in this repository.

```text
Your task is to help me establish and follow a consistent set of professional Jupyter Notebook development standards for my data analytics portfolio.
Every notebook I create must meet professional industry standards. It should function as a reproducible analytical report rather than simply a collection of Python code cells.

The notebook must be understandable to:
- Data Analysts
- Data Scientists
- Business Intelligence Analysts
- Analytics Engineers
- Technical recruiters
- Business stakeholders
Follow this general structure whenever appropriate:
1. Title and metadata
2. Executive summary
3. Business context and analytical objective
4. Research questions or hypotheses
5. Data sources and data dictionary
6. Data preparation and validation
7. Exploratory Data Analysis (EDA)
8. Analytical methodology
9. Analysis and results
10. Business insights and interpretation
11. Limitations and assumptions
12. Recommendations or conclusions
13. References
Adapt the structure to the notebook's actual purpose. Do not force irrelevant sections into simple technical notebooks.

Write the executive summary after completing the analysis, even though it appears at the beginning.
- Use only one H1 (#) title per notebook.
- Use H2 (##) for main sections.
- Use H3 (###) for subsections.
- Introduce every major analytical section with a brief explanation.
- Explain what is being done and why it matters.
- Document important assumptions and methodological decisions.
- Interpret important outputs instead of displaying unexplained results.
- Avoid unnecessary paragraphs and repetitive explanations.
- Maintain consistent terminology.
- Use professional, clear, concise English.
- Never make unsupported claims.
Follow PEP 8 and professional Python conventions.
- Use descriptive variable and function names.
- Keep cells focused on one logical task.
- Avoid unnecessarily long code cells.
- Avoid duplicated code.
- Create reusable functions for repeated operations.
- Use appropriate Pandas and NumPy operations.
- Avoid unnecessary loops and imports.
- Avoid hardcoded machine-specific paths.
- Use pathlib for file paths.
- Use environment variables for credentials and API keys.
- Add comments to explain complex logic and non-obvious decisions.
- Avoid excessive comments explaining obvious code.
- Use appropriate type conversions and validation.
- Keep code readable and maintainable.
For larger projects, recommend moving reusable functions into separate Python modules instead of duplicating them across notebooks.
Always inspect and validate data before conducting analysis.

Check:
- Dataset dimensions
- Column names and data types
- Missing values
- Exact duplicates
- Potential duplicate entities
- Invalid values
- Inconsistent categories
- Outliers
- Data integrity
- Data provenance
Never overwrite original raw data.

Maintain appropriate separation between raw, staging, and processed data.

Document significant transformations and explain why they are necessary.

Do not automatically remove records without establishing a valid reason.
Every chart must answer a relevant analytical question.

Choose visualizations based on their purpose:
- Histogram: distribution
- Bar chart: category comparison
- Scatter plot: relationships
- Box plot: spread and outliers
- Heatmap: correlation or matrix comparisons
- Line chart: temporal patterns
- Geographic map: spatial distribution
- Density map: geographic concentration
Visualization requirements:
- Descriptive titles
- Clearly labeled axes
- Appropriate units
- Readable legends
- Consistent formatting
- Appropriate scales
- Source and date notes when relevant
- Written interpretation below important charts
Avoid unnecessary 3D charts, excessive colors, misleading scales, and decorative visualizations without analytical value.
Before conducting statistical analysis:
1. Define the research question.
2. Identify the unit of analysis.
3. Identify relevant variables.
4. Inspect distributions.
5. Select an appropriate statistical method.
6. Check methodological assumptions.
7. Calculate and validate results.
8. Interpret statistical and practical significance.
9. Document limitations.
Never interpret correlation as causation without sufficient evidence.

Choose statistical methods based on the data and research question, not simply because they are popular.
Whenever a notebook involves machine learning, document:
- Business objective
- Modeling objective
- Input features
- Target variable, if applicable
- Data preparation
- Feature engineering
- Model selection rationale
- Hyperparameters
- Training methodology
- Evaluation metrics
- Model comparison
- Interpretation
- Limitations
Additional requirements:

Clustering
- Explain why clustering is appropriate.
- Standardize features where necessary.
- Justify the number of clusters or parameter choices.
- Evaluate model quality.
- Explain the meaning of each cluster.
Predictive modeling
- Use appropriate train/validation/test strategies.
- Avoid data leakage.
- Compare against a meaningful baseline.
- Select evaluation metrics appropriate to the business problem.
LLM and AI
- Document model name and version.
- Record prompts and expected output schemas.
- Include confidence or uncertainty where appropriate.
- Evaluate outputs against manually verified examples.
- Track API errors and costs when relevant.
- Do not treat AI-generated results as verified ground truth.
Do not introduce deep learning or LLMs without a meaningful analytical justification.
Every notebook must:
- Run from a fresh kernel, top to bottom.
- Avoid dependencies on hidden execution state.
- Specify relevant package dependencies.
- Document data sources and versions.
- Use relative paths.
- Set random seeds where appropriate.
- Store secrets outside the notebook.
- Avoid committing API keys and credentials.
- Use Git version control.
- Include setup instructions where necessary.
Before finalizing, restart the kernel and execute all cells sequentially.
The notebook should look like a professional analytical report.
- Maintain consistent heading hierarchy.
- Use concise Markdown explanations.
- Keep code cells reasonably short.
- Avoid excessive outputs.
- Display only relevant rows from large datasets.
- Use consistent chart dimensions and formatting.
- Maintain a restrained, professional color palette.
- Use descriptive table and chart titles.
- Keep analytical findings visually distinct from code.
- Avoid unnecessary emojis and decorative elements.
Use sequential numbering and descriptive filenames.

Examples:
- 01_data_profiling.ipynb
- 02_data_cleaning.ipynb
- 03_exploratory_data_analysis.ipynb
- 04_statistical_analysis.ipynb
- 05_machine_learning.ipynb
Keep notebooks focused on a clearly defined analytical task.

Avoid combining unrelated analyses into one enormous notebook.
Before considering a notebook complete, review:
- Is the objective clearly defined?
- Are the research questions answered?
- Are data sources documented?
- Is data quality assessed?
- Is the methodology appropriate?
- Is the code readable and maintainable?
- Are visualizations properly labeled?
- Are important outputs interpreted?
- Are conclusions supported by evidence?
- Are limitations documented?
- Is the business relevance clear?
- Can the notebook run from a fresh kernel?
- Is the notebook properly organized for GitHub?
Whenever I ask you to create, edit, improve, or review a Jupyter Notebook:
1. Apply these standards consistently.
2. Preserve the analytical objective and correctness.
3. Do not introduce unnecessary complexity.
4. Explain important methodological decisions.
5. Prefer readable and maintainable code over unnecessarily clever code.
6. Do not fabricate results or data.
7. Do not invent findings before executing or inspecting the relevant analysis.
8. Identify methodological weaknesses and suggest improvements.
9. Make the notebook understandable to both technical and business audiences.
10. Review the complete notebook, not just individual code cells, when the full artifact is available.
If my requested approach violates an important analytical or engineering principle, explain the issue and recommend a better approach rather than blindly following it.

Core principle: Every notebook must be reproducible, technically sound, well-documented, professionally presented, and capable of communicating meaningful analytical insights.

Treat this document as the default Notebook Development Standard for all my data analytics and data science portfolio projects.
```
