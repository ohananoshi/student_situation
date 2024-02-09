#### Tunts Challenge
#### Guilherme Arruda

- #### Problem

##### Update the column "Situação" and "Nota para Aprovação Final" with the constraints below.

$$m=\frac{P1+P2+P3}{3}$$

```
if m < 50       : "Situação" -> "Reprovado por Nota"
if 50 <= m < 70 : "Situação" -> "Exame Final"
if m >= 70      : "Situação" -> "Aprovado"
```

##### If the number in "Faltas" column is bigger than 25% of total classes, column "Situação Final" will be update to "Reprovado por Falta" regardless of m value and the column "Nota para Aprovação Final" will be filled with 0.

##### If the column "Situação" receive the status "Exame final", so the value k that fills the "Nota para Aprovação Final" column will be the nearest integer according:

$$k\:=\:100\:-\:m$$

##### If the column "Situação" receive the status "Aprovado", "Nota para Aprovação Final" column will be filled with 0.

#### Sample Table

| Matricula | Aluno    | Faltas | P1  | P2  | P3  | Situação     | Nota para Aprovação Final |
|-----------|----------|--------|-----|-----|-----|--------------|---------------------------|
| 1         | Eduardo  | 8      | 35  | 63  | 61  | Exame Final  | 47                        |


- #### Running

```md
This code use python use python 3.12
Depencies: gspread, pandas

git clone https://github.com/ohananoshi/student_situation.git

cd student_situation

mkdir Credentials

# You must be put authentication .json files in this directory

py -m venv venv

venv/Scripts/activate

venv/Scripts/python -m pip install --upgrade gspread pandas

venv/Scripts/python main.py
```

