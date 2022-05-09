from generate import *
from faker import Faker

login = 'neo4j'
password = 'iXkWvm40MmK1bSVHKUPcK9QZsQuOgwNZCu44h1n4jWc'

config.DATABASE_URL = f'bolt://{login}:{password}@localhost:7687'

fake = Faker()


def generate_all_silent():
    # nodes
    generate_administrators()
    generate_adm_employees()
    generate_drivers()
    generate_doctors()
    generate_medics()
    generate_supervisors()
    generate_locations()
    generate_medical_facilities()
    generate_hospital_wards()
    generate_vehicles()
    generate_transfers()
    generate_patients()
    generate_referrals()
    generate_medical_exams()
    # relationships
    generate_creates()
    generate_is_reserved()
    generate_is_in()
    generate_executed_by()
    generate_books()
    generate_is_from()
    generate_is_to()
    generate_overseen_by()
    generate_works()
    generate_manages()
    generate_owns()
    generate_belongs_to_has()
    generate_offers()
    generate_is_occupied_occupies_place()
    generate_participates()
    generate_gets()
    generate_issued_by()
    generate_concerns()


def generate_all_verbose():
    # nodes
    generate_administrators()
    print("Generating Administrators finished")
    generate_adm_employees()
    print("Generating Administrative Employees finished")
    generate_drivers()
    print("Generating Drivers finished")
    generate_doctors()
    print("Generating Doctors finished")
    generate_medics()
    print("Generating Medics finished")
    generate_supervisors()
    print("Generating Supervisors finished")
    generate_locations()
    print("Generating Locations finished")
    generate_medical_facilities()
    print("Generating Medical Facilities finished")
    generate_hospital_wards()
    print("Generating Hospital Wards finished")
    generate_vehicles()
    print("Generating Vehicles finished")
    generate_transfers()
    print("Generating Transfers finished")
    generate_patients()
    print("Generating Patients finished")
    generate_referrals()
    print("Generating Referrals finished")
    generate_medical_exams()
    print("Generating Medical Exams finished")

    # relationships
    generate_creates()
    print("Generating relationship CREATES finished")
    generate_is_in()
    print("Generating relationship IS IN finished")
    generate_is_reserved()
    print("Generating relationship IS RESERVED finished")
    generate_executed_by()
    print("Generating relationship EXECUTED BY finished")
    generate_books()
    print("Generating relationship BOOKS finished")
    generate_is_from()
    print("Generating relationship IS FROM finished")
    generate_is_to()
    print("Generating relationship IS TO finished")
    generate_overseen_by()
    print("Generating relationship OVERSEEN BY finished")
    generate_works()
    print("Generating relationship WORKS finished")
    generate_manages()
    print("Generating relationship MANAGES finished")
    generate_creates()
    print("Generating relationship CREATES finished")
    generate_owns()
    print("Generating relationship OWNS finished")
    generate_belongs_to_has()
    print("Generating relationships BELONGS TO and HAS finished")
    generate_offers()
    print("Generating relationship OFFERS finished")
    generate_is_occupied_occupies_place()
    print("Generating relationships IS OCCUPIED and OCCUPIES PLACE finished")
    generate_participates()
    print("Generating relationship PARTICIPATES finished")
    generate_gets()
    print("Generating relationship GETS finished")
    generate_issued_by()
    print("Generating relationship ISSUED BY finished")
    generate_concerns()
    print("Generating relationship CONCERNS finished")
    print()
    print("-------------------------Database generated :)")


if __name__ == '__main__':
    generate_all_verbose()
    # generate_all_silent()

    # MATCH (n) DETACH DELETE n
