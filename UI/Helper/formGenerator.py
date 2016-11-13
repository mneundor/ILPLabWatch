from bs4 import BeautifulSoup
#this file contains helper functions to generate forms

#returns a form tag. formType is form-horizontal or form-inline
def getFormTag(method, action, formType = ""):
    bs = BeautifulSoup("", "html.parser")
    formTag = bs.new_tag("form", method=method, action=action)
    formTag["class"] = formType
    bs.append(formTag)
    return bs

#adds a submit Button to the form.
def addSubmitButton(formTag, lable):
    buttonTag = formTag.new_tag("button")
    buttonTag["type"] = "submit"
    buttonTag["class"] = "btn btn-primary"
    buttonTag.string = lable
    formTag.insert(buttonTag)

#adds a Radioselector to the form. Radios is a dict
def addRadioSelector(formTag, lable, name, radios):
    divTag = helperGetDivAround()

    headingLable = formTag.new_tag("lable")
    headingLable["for"] = name
    headingLable.string = lable
    divTag.div.insert(headingLable)

    for key, value in radios.items():
        #generate formal html code for each element
        outDiv = formTag.new_tag("div")
        outDiv["class"] = "radio"
        lableTag = formTag.new_tag("lable")
        outDiv.insert(lableTag)

        #generate the inputTag
        inputTag = formTag.new_tag("input", type="radio", id="radio-" + key,  value=value["value"])
        if value["disabled"] == True:
            inputTag["disabled"] = "disabled"
        lableTag.insert(inputTag)
        lableTag.insert(value["optionText"])
        divTag.insert(outDiv)

    formTag.insert(divTag)

def helperGetDivAround():
    bs = BeautifulSoup("", "html.parser")
    divTag =  bs.new_tag("div")
    divTag["class"] = "form-group"
    bs.append(divTag)
    return bs