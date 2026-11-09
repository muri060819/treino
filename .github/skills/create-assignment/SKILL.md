---
name: create-assignment
description: "Use when creating a new educational programming assignment, adding a task to the student portal, updating config.json, or preparing starter code and sample data for an assignment."
---

# Creating an Assignment

Create a complete, student-friendly assignment for this repository and register it in the static site.

## Workflow

1. **Understand the assignment.** Identify the topic, learning goals, student level, programming language, expected deliverables, and any due date. Ask focused questions only for information needed to make a correct assignment or portal entry. Do not invent a due date or claim that optional files were requested.
2. **Inspect project conventions.** Read `.github/instructions/assignments.instructions.md`, `templates/assignment-template.md`, and `config.json`. Review a relevant existing assignment and its starter files when useful. Check that the proposed assignment ID and directory do not already exist. Never overwrite existing assignment content without permission.
3. **Create the assignment folder and README.** Use a descriptive lowercase kebab-case folder name under `assignments/` and create `assignments/<id>/README.md`. Follow the template and assignment instructions exactly:
   - Use `# 📘 Atividade: [Título da Atividade]`, `## 🎯 Objetivo`, and `## 📝 Tarefas`.
   - Write the objective in 1–2 clear sentences focused on what students will learn or build.
   - Give each task a specific, action-oriented `### 🛠️` heading followed by `#### Descrição` and `#### Requisitos`.
   - Make requirements concrete and verifiable. Include code or input/output examples when they help students understand the expected behavior.
   - Write in clear, encouraging Portuguese appropriate to the students. Do not add sections not present in the template unless requested.
4. **Add optional learning files only when appropriate.** Ask whether starter code or sample data is needed if the request does not say. Keep assignment files in its folder and use the repository-supported names `starter-code.py` and `data.csv` where applicable. Starter code should run or clearly indicate what students should complete; sample data should be small, valid, and directly useful for the tasks. Do not create empty or unrelated attachments.
5. **Register the assignment.** Add one entry to the `assignments` array in `config.json` with:
   - `id`: the unique kebab-case folder name;
   - `title`: a concise portal title;
   - `description`: a short summary for students;
   - `path`: `assignments/<id>`;
   - `dueDate`: an ISO `YYYY-MM-DD` date only when one is provided;
   - `attachments`: only when files are included, using each file's name, relative filename, and type, consistent with existing entries.
   
   Preserve existing entries and the JSON formatting. Ensure each configured attachment exists in that assignment folder.
6. **Validate the complete change.** Parse `config.json` as JSON; confirm the new ID is unique, its path points to the new folder, the README and any configured attachments exist, and the README contains the required headings and task subsections. Review the diff to ensure unrelated assignments and files are unchanged. Report the created files and any checks performed.

## Repository references

- Assignment authoring rules: [`.github/instructions/assignments.instructions.md`](../../instructions/assignments.instructions.md)
- Required assignment structure: [`templates/assignment-template.md`](../../../templates/assignment-template.md)
