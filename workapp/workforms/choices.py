from django.db import models

class Choices(models.Model):
    JOB_TYPE = [
        ("Door Callout", "Door Callout"),
        ("Door Service", "Door Service"),
        ("Door Installation", "Door Installation"),
        ("Gate Callout", "Gate Callout"),
        ("Gate Service", "Gate Service"),
        ("Gate Installation", "Gate Installation"),
        ("Electrical Callout", "Electrical Callout"),
        ("Electrical Service", "Electrical Service"),
        ("Electrical Installation", "Electrical Installation"),
        ("Other", "Other"),
    ]

    INSTALLATION = [
        ("Swing Door", "Swing Door"),
        ("Slide Door", "Slide Door"),
        ("Fold Door", "Fold Door"),
    ]

    CONDITION = [
        ("Good", "Good"),
        ("Requires Replacement", "Requires Replacement"),
        ("Requires Attention", "Requires Attention"),
        ("Replaced", "Replaced"),
        ("Repaired", "Repaired"),
        ("N/A", "N/A)"),
    ]

    SELECTOR = [
        ("BDE-D", "BDE-D"),
        ("BDE-K", "BDE-K"),
        ("BDE-M", "BDE-M"),
        ("Other", "Other"),
    ]

    ARM_TYPE = [
        ("Push Arm","Push Arm"),
        ("Slide Arm", "Slide Arm"),
        ("Articulated Arm","Articulated Arm"),
    ]

    DOOR_TYPE = [
        ("Aluminum", "Aluminum"),
        ("Wood", "Wood"),
        ("Glass Door", "Glass Door"),
    ]

    SENSOR = [
        ("RIC290", "RIC290"),
        ("RAD290", "RAD290"),
        ("AIS290", "AIS290"),
        ("HR100", "HR100"),
        ("HR94", "HR94"),
        ("HR54", "HR54"),
        ("Domino", "Domino"),
        ("BER Activation", "BER Activation"),
        ("Record Swing", "Record Swing"),
        ("Hotron Swing", "Hotron Swing"),
        ("WF Button", "WF Button"),
        ("Button", "Button"),
        ("Swipe Card", "Swipe Card"),
        ("Eye Beams", "Eye Beams"),
        ("N/A", "N/A"),
    ]

    STATUS = [
        ("Created", "Created"),
        ("Pending Approval", "Pending Approval"),
        ("Invoiced", "Invoiced"),
        ("Emailed", "Emailed"),
        ("Complete", "Complete"),
    ]

    stock_location = [
        ("Van", "Van"),
        ("Stores", "Stores"),
    ]
