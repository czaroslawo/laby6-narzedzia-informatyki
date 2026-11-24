from models import Parameters, Apartment, Tenant, Bill
from src.manager import Manager

def test_total_due_pln():
    parameters = Parameters()
    manager = Manager(parameters)
    for apartment in manager.apartments.values():
        settlement = manager.get_settlement(apartment.key, 2025, 1)
        assert settlement.total_due_pln == manager.get_apartment_costs(
            apartment.key, 2025, 1
        )

def test_check_deposit():
    parameters = Parameters()
    manager = Manager(parameters)
    tenant = Tenant(
        name='Test Tenant',
        apartment='apart-test',
        room='test-room',
        apartment_key='apart-test',
        rent_pln=1500.0,
        deposit_pln=3000.0,
        date_agreement_from='2024-01-01',
        date_agreement_to='2024-12-31'
    )
    bills = [
        Bill(
            amount_pln= 1500.00,
            date_due= "2025-02-15",
            settlement_year= 2025,
            settlement_month= 1,
            apartment= "apart-polanka",
            type= "deposit"
        ),
        Bill(
            amount_pln=1500.00,
            date_due="2025-02-15",
            settlement_year=2025,
            settlement_month=1,
            apartment="apart-polanka",
            type="deposit"
        ),
    ]
    manager.bills = bills
    manager.tenants = {"test-tenant": tenant}

    assert manager.check_deposit(tenant)


