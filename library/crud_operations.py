
class CRUDOperations:
 
    @staticmethod
    def getAllData(model, serializer):
        allObjects = model.objects.all()
        serializedData = serializer(allObjects, many=True).data
        return serializedData
        
    @staticmethod
    def getSpecificData(model, serializer, **condition) -> dict:
        try:
            specificObject = model.objects.get(**condition)
            serializedData = serializer(specificObject).data
            return {'status' : True, 'data' : serializedData}
        except:
            return {'status' : False}
        
    @staticmethod
    def getFilteredData(model, serializer, **args) -> list[dict]:
        getExistingObjects = model.objects.filter(**args)
        serializedData = serializer(getExistingObjects, many=True).data
        return serializedData
    
    @staticmethod
    def addNewData(serializer, data) -> dict:
        serializedData = serializer(data=data)
        if serializedData.is_valid():
            serializedData.save()
            return {'status' : True, 'data' : serializedData.data}
        else:
            return {'status' : False}
    
    @staticmethod
    def updateExistingData(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False}
    @staticmethod
    def updateExistingDataUniv(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(university_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False}   
    @staticmethod
    def updateExistingDataCou(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(course_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False}   
    @staticmethod
    def updateExistingDataDeg(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(degree_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    @staticmethod
    def updateExistingDataYrs(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(year_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    
    @staticmethod
    def updateExistingDataSem(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(semester_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    
    @staticmethod
    def updateExistingDataExm(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(exam_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    
    @staticmethod
    def updateExistingDataSch(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(school_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    @staticmethod
    def updateExistingDataCls(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(class_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False}   
    
    @staticmethod
    def updateExistingDataSub(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(subject_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    @staticmethod
    def updateExistingDataVid(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(video_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False} 
    @staticmethod
    def updateExistingDataFile(model, serializer, id, data) -> dict:
        try:
            getOldObject = model.objects.get(file_id=id)
            serializedData = serializer(getOldObject, data=data, partial=True)
            if serializedData.is_valid():
                serializedData.save()
                return {'status' : True, 'data' : serializedData.data}
            else:
                return {'status' : False}
        except:
            return {'status' : False}    
#....DELETE Methods   
    @staticmethod
    def deleteExistingData(model, id) -> bool:
        try:
            model.objects.get(id=id).delete()
            return True
        except:
            return False

    @staticmethod
    def deleteExistingDataUniv(model, id) -> bool:
        try:
            model.objects.get(university_id=id).delete()
            return True
        except:
            return False
        
    @staticmethod
    def deleteExistingDataCou(model, id) -> bool:
        try:
            model.objects.get(course_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataDeg(model, id) -> bool:
        try:
            model.objects.get(degree_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataYrs(model, id) -> bool:
        try:
            model.objects.get(year_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataSem(model, id) -> bool:
        try:
            model.objects.get(semester_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataExm(model, id) -> bool:
        try:
            model.objects.get(exam_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataSch(model, id) -> bool:
        try:
            model.objects.get(school_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataCls(model, id) -> bool:
        try:
            model.objects.get(class_id=id).delete()
            return True
        except:
            return False
    @staticmethod
    def deleteExistingDataSub(model, id) -> bool:
        try:
            model.objects.get(subject_id=id).delete()
            return True
        except:
            return False
        
    @staticmethod
    def deleteExistingDataVid(model, id) -> bool:
        try:
            model.objects.get(video_id=id).delete()
            return True
        except:
            return False
    
    @staticmethod
    def deleteExistingDataFile(model, id) -> bool:
        try:
            model.objects.get(file_id=id).delete()
            return True
        except:
            return False
  