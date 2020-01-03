# some file to make the folder a python package
from .views import app

# turn off the graph db dependency
# from .models import graph


#graph.delete_all()
# turn off the graph db dependency
# if not graph.schema.get_uniqueness_constraints("User") :
#     graph.schema.create_uniqueness_constraint("User", "username")
# if not graph.schema.get_uniqueness_constraints("Tag") :
#     graph.schema.create_uniqueness_constraint("Tag", "name")
# if not graph.schema.get_uniqueness_constraints("Post") :
#     graph.schema.create_uniqueness_constraint("Post", "id")

# create the database from scratch
query= """
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///C:/Users/keir2/Downloads/PersonTreatmentAppointmentAssesmentFlatNoSpaces.csv" AS row
CREATE (:PersonFlat {
PERSON_ID: row.PERSON_ID,
Gender: row.Gender,
EthnicCategory: row.EthnicCategory,
ExBritishArmedForces: row.ExBritishArmedForces,
AGE_END_REPORTING_PERIOD: row.AGE_END_REPORTING_PERIOD,
AGE_START_REPORTING_PERIOD: row.AGE_START_REPORTING_PERIOD,
LongTermCondition: row.LongTermCondition,
ReligiousBelief: row.ReligiousBelief,
OrganisationName: row.OrganisationName,
OrgTypeDaily: row.OrgTypeDaily,
AppointmentPurpose: row.AppointmentPurpose,
AddendanceDescription: row.AddendanceDescription,
ConsultationMedium: row.ConsultationMedium,EmploymentStatus: row.EmploymenyStatus,
DisabilityDescription: row.DisabilityDescription,
ReceivingSickPay: row.ReceivingSickPay,
SexualOrientationDesc: row.SexualOrientationDesc,
ShortNoticeCancellation: row.ShortNoticeCancellation,
SteppedCareIntensity: row.SteppedCareIntensity,
TherapyIntensity: row.TherapyIntensity,
TherapyType: row.TherapyType,
UseofPsychotropicMedication: row.UseofPsychotropicMedication,
DidStaffListenToYouAndTreatYourConcernsSeriously: row.DidStaffListenToYouAndTreatYourConcernsSeriously,
DidYouFeelInvolvedInMakingChoicesAboutYourTeatmentAndCare: row.DidYouFeelInvolvedInMakingChoicesAboutYourTeatmentAndCare,
DidYouHaveConfidenceInYourTherapistAndHisOrHerSkillsAndtechniques: row.DidYouHaveConfidenceInYourTherapistAndHisOrHerSkillsAndtechniques,
HasTheServiceHelpedYouToBetterUnderstandAndAddressYourDifficulties: row.HasTheServiceHelpedYouToBetterUnderstandAndAddressYourDifficulties,
OnReflectionDidYouGetTheHelpThatMatteredToYou: row.OnReflectionDidYouGetTheHelpThatMatteredToYou
});"""

#graph.run(query)

# this works
#graph.evaluate(query)

