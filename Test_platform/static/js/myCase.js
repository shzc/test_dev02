
//获取项目列表
var ProjectInit = function(_cmbProject) {
    var cmbProject = document.getElementById(_cmbProject);
    var options = "";

    //创建下拉选项
    function cmbAddOption(cmb,project_obj) {
        console.log(project_obj);
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = project_obj.name;
        option.value = project_obj.id;
    }

    function getProjectListInfo() {
        //获取用例信息
        $.get("/project/get_project_list/",{},function (resp){
            if (resp.status == 10200) {
                console.log(resp.data);
            //遍历项目
                let dataList = resp.data;

                for (var i = 0; i < dataList.lenght; i++) {
                    cmbAddOption(cmbProject,dataList[i]);
                };

            } else {
                window.alert(resp.message);
            }

            });
    };

    //调用
    getProjectListInfo();
};
