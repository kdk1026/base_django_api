from dataclasses import asdict, dataclass
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Person 객체 정의
@dataclass
class Person:
    seq: int
    name: str
    age: int

    def to_dict(self):
        return asdict(self)
    
# 메모리 DB 역할을 할 리스트
person_list = [
    Person(1, "홍길동", 20),
    Person(2, "임꺽정", 25)
]

NOT_FOUND = "Not Found"

# 테스트 편의를 위해 CSRF 비활성화
@method_decorator(csrf_exempt, name='dispatch')
class PersonAPI(View):

    # GET /sample/persons or /sample/persons/{seq}
    def get_persons(self, request, seq=None):
        if seq:
            person = next((p for p in person_list if p.seq == seq), None)
            if person:
                return JsonResponse(person.to_dict())
            return JsonResponse({"error": NOT_FOUND}, status=404)
        return JsonResponse([p.to_dict() for p in person_list], safe=False)
    
    # POST /sample/persons
    def add_person(self, request):
        data = json.loads(request.body)
        new_seq = person_list[-1].seq + 1 if person_list else 1
        new_person = Person(new_seq, data['name'], data['age'])
        person_list.append(new_person)
        return JsonResponse({"result": "success"}, status=201)
    
    # PUT /sample/persons
    def update_person(self, request):
        data = json.loads(request.body)
        person = next((p for p in person_list if p.seq == data['seq']), None)
        if person:
            person.name = data.get('name', person.name)
            person.age = data.get('age', person.age)
            return JsonResponse({"result": "success"})
        return JsonResponse({"error": NOT_FOUND}, status=404)
    
    # DELETE /sample/persons/{seq}
    def delete_person(self, request, seq):
        global person_list
        person = next((p for p in person_list if p.seq == seq), None)
        if person:
            person_list = [p for p in person_list if p.seq != seq]
            return JsonResponse({"result": "success"})
        return JsonResponse({"error": NOT_FOUND}, status=404)

