################################### �޸���� BR_J�� �߰����� ����. ###################################
def seperate_diaper_brand(x):
    ############# �ϱ⽺ #############
    if '�ϱ⽺' in x:
        return '�ϱ⽺'
    ############# �� #############
    elif '��' in x:
        return '��'
    ############# �޸��� #############
    elif '�޸���' in x:
        return '�޸���'
    ############# ���۽� #############
    elif '���۽�' in x:
        return '���۽�'
    ############# �������� #############
    elif '��������' in x:
        return '��������'
    ############# ������ #############
    elif '������' in x:
        return '������'
    ############# ����ó����޷� #############
    elif '�����' in x:
        return '����ó����޷�'
    ############# ���۴�� #############
    elif '���۴��' in x:
        return '���۴��'
    ############# ��ڷ��� #############
    elif '��ڷ���' in x:
        return '��ڷ���'
    ############# Ų�� #############
    elif 'Ų��' in x:
        return 'Ų��'
    ############# ������ #############
    elif '������' in x:
        return '������'
    else:
        pass  
########################## �ϱ⽺ �귣�� �з� ##########################
def haggies_j(x):
    if '����' in x:
        return '���ۺ���'
    elif '����' in x:
        return '������'
    elif '����ó���̵�' in x:
        return '����ó���̵�'
    elif '����ּ�' in x:
        return '����ּ�'
    elif '�ƽ������' in x:
        return '�ƽ������'
    elif 'ũ������' in x:
        return 'ũ������'
    elif '��������Ʈ' in x:
        return '��������Ʈ'
    else:
        return '�ϱ⽺_��Ÿ'
########################## �� �귣�� �з� ##########################
def goon_j(x):
    if '��������' in x:
        return '��������'
    elif '���ø��' in x:
        return '���ø��'
    elif '����' in x:
        return '����'
    elif '����Ʈ' in x:
        return '������'
    elif '���ۺ�' in x:
        return '���ۺ�'
    elif '����' in x:
        return '����'
    elif '������' in x:
        return '������'
    elif '���' in x:
        return '���'
    else:
        return '��_��Ÿ'
########################## ���۽� �귣�� �з� ##########################
def pampers_j(x):
    if '���̺�' in x:
        return '���̺� �����'
    elif '�����' in x:
        return 'ũ����/��Ƽ����'
    elif '��Ƽ��' in x:
          return 'ũ����/��Ƽ����'
    elif '���͵鷯' in x:
        return '���͵鷯'
    else:
        return '���۽�_��Ÿ'
########################## ������ũ �귣�� �з� ##########################
def mammypoko_j(x):
    if '�������' in x:
        return '�������'
    elif '360' in x:
        return '360�� ��Ƽ'
    elif '����' in x:
        return '����'
    elif '�������' in x:
        return '�������'
    elif '�¹�' in x:
        return '�¹�'
    elif '����' in x:
        return '���������Ƽ'
    elif '��������' in x:
        return '��������'
    elif '������' in x:
        return '������'
    else:
        return '������ũ_��Ÿ'
########################## ������ �귣�� �з� ##########################
def bosomi_j(x):
    if '������ư' in x:
        return '������ư'
    elif '������ư���' in x:
        return '������ư���'
    elif '�׼���' in x:
        return '�׼���'
    elif '�������' in x:
        return '�������'
    elif '������' in x:
        return '������'
    elif '���̺��ɾ�' in x:
        return '���̺��ɾ�'
    else:
        return '������_��Ÿ'
########################## ����ó��޷� �귣�� �з� ##########################
def naturel_j(x):
    if '��������' in x:
        return '��������'
    elif '����' in x:
        return '����'
    elif '����' in x:
        return '����'
    else:
        return '����ó����޷�_��Ÿ'
########################## ���۴�� �귣�� �з� ##########################
def superdady_j(x):
    if '����' in x:
        return '��������'
    elif '����Ʈ' in x:
        return '�������Ʈ'
    elif '����' in x:
        return '���󽽸�'
    else:
        return '���۴��_��Ÿ'
######################### ��ڷ��� �귣�� �з� ##########################
def penelope_j(x):
    if '��ħ' in x:
        return '��ħ����'
    elif '��Ű' in x:
        return '��Ű����'
    elif '��' in x:
        return '������'
    elif '�̶�Ŭ' in x:
        return '�̶�Ŭ'
    else:
        return '��ڷ���_��Ÿ'
########################## Ų�� �귣�� �з� #########################
def kindoh_j(x):
    if '�����̾�' in x:
        return '�����̾�'
    elif '����' in x:
        return '��������'
    elif '����' in x:
        return '�����÷���'
    else:
        return 'Ų��_��Ÿ'
######################### ������ �귣�� �з� ##########################
def nabijam_j(x):
    if '��Ʈ��' in x:
        return '��Ʈ���'
    elif '����' in x:
        return '��������Ʈ'
    elif '����' in x:
        return '���۵����'
    elif '����' in x:
        return '����'
    else:
        return '������_��Ÿ'