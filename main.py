import logging
import pandas as pd
import gspread

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Info
CREDENTIAL_NAME = "Credentials/credential.json"
TOKEN_NAME = "Credentials/token.json"
SPREADSHEET_ID = "1ENc8K0T1_T64jkc6CZLPMxuceQcBfJBwDxt2jwPvTi8"
SHEET_NAME = "engenharia_de_software"

#Try to connect
try:
    client = gspread.oauth(credentials_filename=CREDENTIAL_NAME,
                           authorized_user_filename=TOKEN_NAME)
    
    #Open spreadsheet
    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    #Select worksheet
    folha = spreadsheet.worksheet(SHEET_NAME)

except FileNotFoundError:
    logger.error("Login Failed: credentials or token files not found.")
except gspread.exceptions.SpreadsheetNotFound:
    logger.error("Acces Failed: spreadsheet not found.")
except gspread.exceptions.WorksheetNotFound:
    logger.error("Acces Failed: worksheet not found")
else:
    logger.info("Conection succesfull.")


logger.info("Reading data.")
max_absences = int(folha.acell('A2').value.split(": ")[1])*0.25

data = pd.DataFrame(folha.get_all_values("C4:F27"), columns=folha.get_all_values("C3:F3"))
data = data[['Faltas','P1','P2','P3']].astype(int)

logger.info("Student situation and grade calculating.")
mean_list = data[['P1','P2','P3']].mean(axis=1)

student_state = []
approval_grade = []

for i in range(len(mean_list)):
    if data['Faltas'].iloc[i,0] > max_absences:
        student_state.append(['Reprovado por Falta'])
        approval_grade.append(['0'])
    else :
        if mean_list[i] < 50.0:
            student_state.append(['Reprovado por Falta'])
            approval_grade.append(['0'])
        elif 50.0 <= mean_list[i] < 70.0:
            student_state.append(['Exame Final'])
            approval_grade.append([str(int(100 - mean_list[i]))])
        else :
            student_state.append(['Aprovado'])
            approval_grade.append(['0'])

logger.info("Updating 'Situação Final' column")
folha.update(range_name="G4:G27", values=student_state)

logger.info("Updating 'Nota para Aprovação Final' column")
folha.update(range_name="H4:H27", values=approval_grade, raw=False)