const handleAddons = (name, data) => {
  if (selectedAddon.length === 0){
    const x = {}
    x["addonName"] = name
    x["data"] = [data]
    selectedAddon = [...selectedAddon, x]
  }else{
    for(var x in selectedAddon){
      if(selectedAddon[x]["addonName"] === name){
        if (selectedAddon[x]["data"].includes(data)){
          selectedAddon[x]["data"] = selectedAddon[x]["data"].filter(p => p !== data)
          if (selectedAddon[x]["data"].length === 0){
            selectedAddon = selectedAddon.filter(p => p["addonName"] !== name)
            return selectedAddon
          }
          return selectedAddon
        }
        selectedAddon[x]["data"] = [...selectedAddon[x]["data"], data]
        return selectedAddon
      }
    }
    const z = {}
    z["addonName"] = name
    z["data"] = [data]
    selectedAddon = [...selectedAddon, z]
  }
  return selectedAddon
}
