(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6788b418"],{"0f7c":function(t,e,a){},"432b":function(t,e,a){"use strict";a.d(e,"a",(function(){return i}));var s=a("5530"),r=a("5880"),i={computed:Object(s["a"])(Object(s["a"])({},Object(r["mapState"])({layout:function(t){return t.app.layout},navTheme:function(t){return t.app.theme},primaryColor:function(t){return t.app.color},colorWeak:function(t){return t.app.weak},fixedHeader:function(t){return t.app.fixedHeader},fixedSidebar:function(t){return t.app.fixedSidebar},contentWidth:function(t){return t.app.contentWidth},autoHideHeader:function(t){return t.app.autoHideHeader},isMobile:function(t){return t.app.isMobile},sideCollapsed:function(t){return t.app.sideCollapsed},multiTab:function(t){return t.app.multiTab}})),{},{isTopMenu:function(){return"topmenu"===this.layout}}),methods:{isSideMenu:function(){return!this.isTopMenu}}}},"620e":function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a-card",[t.orderDetail?a("page-header-wrapper",{attrs:{title:t.orderDetail.title},scopedSlots:t._u([{key:"content",fn:function(){return[a("a-descriptions",{attrs:{size:"small",column:t.isMobile?1:2}},[a("a-descriptions-item",{attrs:{label:"申请人"}},[t._v(t._s(t.orderDetail.applicant))]),a("a-descriptions-item",{attrs:{label:"备注"}},[t._v(t._s(t.orderDetail.remark))]),a("a-descriptions-item",{attrs:{label:"工单环境"}},[a("span",{staticStyle:{color:"red"}},[t._v(t._s(t.orderDetail.env_id))])]),a("a-descriptions-item",{attrs:{label:"工单类型"}},[t._v(t._s(t.orderDetail.sql_type))]),a("a-descriptions-item",{attrs:{label:"DB类型"}},[t._v(t._s(t.orderDetail.display_rds_category))]),a("a-descriptions-item",{attrs:{label:"DB实例"}},[t._v(t._s(t.orderDetail.host+":"+t.orderDetail.port))]),a("a-descriptions-item",{attrs:{label:"库名"}},[a("span",{staticStyle:{color:"blue"}},[t._v(t._s(t.orderDetail.database))])]),a("a-descriptions-item",{attrs:{label:"创建时间"}},[t._v(t._s(t.orderDetail.created_at))]),a("a-descriptions-item",{attrs:{label:"需求"}},[t._v(t._s(t.orderDetail.demand))])],1)]},proxy:!0},{key:"extraContent",fn:function(){return[a("a-row",{staticClass:"status-list"},[a("a-col",{attrs:{xs:24,sm:24}},[a("div",{staticClass:"text"},[t._v("状态")]),a("div",{staticClass:"heading"},[a("h2",[t._v(t._s(t.orderDetail.progress))])])])],1)]},proxy:!0},{key:"extra",fn:function(){return[a("a-button-group",{staticStyle:{"margin-right":"4px"}},[a("a-button",{attrs:{type:"dashed",disabled:t.btnStatus.btnDisabled,icon:"retweet"},on:{click:t.showModal}},[t._v(" "+t._s(t._f("btnTitle")(t.orderDetail.progress))+" ")]),"已复核"===t.orderDetail.progress?a("a-button",{attrs:{icon:"link"},on:{click:t.showHookModal}},[t._v("钩子")]):t._e(),a("a-button",{attrs:{type:"dashed",disabled:t.btnStatus.closeDisabled,icon:"close-circle"},on:{click:t.showCloseModal}},[t._v("关闭工单")]),a("a-button",{attrs:{type:"dashed",loading:t.executeLoading,icon:"thunderbolt"},on:{click:t.generateSqlOrdersTasks}},[t._v("执行工单")]),["处理中","已完成","已复核","已勾住"].includes(t.orderDetail.progress)?a("a-button",{attrs:{type:"dashed",icon:"eye"},on:{click:t.showTasksDrawer}},[t._v("子任务详情")]):t._e(),a("a-button",{attrs:{type:"dashed",loading:t.loading,icon:"sync"},on:{click:t.refresh}},[t._v("刷新")])],1),a("a-modal",{attrs:{title:"请输入[可选]"},model:{value:t.visible,callback:function(e){t.visible=e},expression:"visible"}},[a("a-textarea",{attrs:{rows:"3",autoSize:{minRows:3,maxRows:5}},model:{value:t.confirmMsg,callback:function(e){t.confirmMsg=e},expression:"confirmMsg"}}),a("template",{slot:"footer"},[a("a-button",{key:"back",on:{click:t.handleCancel}},[t._v(t._s(t.confirmBtnTips.cancelText))]),a("a-button",{key:"submit",attrs:{type:"primary",loading:t.loading},on:{click:t.handleOk}},[t._v(" "+t._s(t.confirmBtnTips.okText)+" ")])],1)],2),a("a-modal",{attrs:{title:"请输入[可选]"},model:{value:t.closeVisible,callback:function(e){t.closeVisible=e},expression:"closeVisible"}},[a("a-textarea",{attrs:{rows:"3",autoSize:{minRows:3,maxRows:5}},model:{value:t.confirmMsg,callback:function(e){t.confirmMsg=e},expression:"confirmMsg"}}),a("template",{slot:"footer"},[a("a-button",{key:"back",on:{click:t.handleCloseCancel}},[t._v("关闭")]),a("a-button",{key:"submit",attrs:{type:"primary",loading:t.loading},on:{click:t.handleCloseOk}},[t._v("提交")])],1)],2),a("a-modal",{attrs:{title:"请选择目标环境[钩子]",width:"35%"},model:{value:t.hookVisible,callback:function(e){t.hookVisible=e},expression:"hookVisible"}},[a("el-form",{ref:"ruleForm",attrs:{model:t.ruleForm,"label-width":"150px",size:"small"}},[a("el-form-item",{attrs:{label:"当前工单"}},[a("el-input",{staticStyle:{width:"95%"},attrs:{readonly:"",placeholder:"请输入标题"},model:{value:t.ruleForm.title,callback:function(e){t.$set(t.ruleForm,"title",e)},expression:"ruleForm.title"}})],1),a("el-form-item",{attrs:{label:"当前库"}},[a("el-input",{staticStyle:{width:"95%"},attrs:{readonly:"",placeholder:"请输入需求描述"},model:{value:t.ruleForm.current_database,callback:function(e){t.$set(t.ruleForm,"current_database",e)},expression:"ruleForm.current_database"}})],1),a("el-form-item",{attrs:{label:"目标环境"}},[a("el-select",{staticStyle:{width:"95%"},attrs:{placeholder:"请选择工单环境",value:""},on:{change:t.changeEnvs},model:{value:t.ruleForm.env_id,callback:function(e){t.$set(t.ruleForm,"env_id",e)},expression:"ruleForm.env_id"}},t._l(t.sql_envs,(function(t){return a("el-option",{key:t.id,attrs:{label:t.name,value:t.id,disabled:t.disabled}})})),1)],1),a("el-form-item",{attrs:{label:"目标库"}},[a("el-select",{staticStyle:{width:"95%"},attrs:{clearable:"",filterable:"",placeholder:"请选择目标数据库",value:""},model:{value:t.ruleForm.database,callback:function(e){t.$set(t.ruleForm,"database",e)},expression:"ruleForm.database"}},t._l(t.schemas,(function(t){return a("el-option",{key:t.id,attrs:{label:t.comment+"-"+t.schema,value:t.cid+"__"+t.schema}})})),1)],1),a("el-form-item",{attrs:{label:"审核状态"}},[a("a-switch",{attrs:{"checked-children":"重置审核状态为：待审批","un-checked-children":"继承审核状态为：已批准","default-checked":""},on:{change:t.onRestChange}})],1),a("el-form-item",{attrs:{label:"备注"}},[a("el-select",{staticStyle:{width:"95%"},attrs:{placeholder:"请选择合适的备注",value:""},model:{value:t.ruleForm.remark,callback:function(e){t.$set(t.ruleForm,"remark",e)},expression:"ruleForm.remark"}},t._l(t.remarks,(function(t){return a("el-option",{key:t,attrs:{label:t,value:t}})})),1)],1)],1),a("template",{slot:"footer"},[a("a-button",{key:"back",on:{click:t.handleHookCancel}},[t._v("关闭")]),a("a-button",{key:"submit",attrs:{type:"primary",loading:t.hookLoading},on:{click:t.handleHookOk}},[t._v("提交")])],1)],2)]},proxy:!0}],null,!1,3016291350)},[a("a-card",{staticStyle:{"margin-top":"-10px"},attrs:{bordered:!1,title:"事件进度"}},[a("a-steps",{attrs:{current:t.currentStatus,size:"small"}},[a("a-step",{attrs:{title:"创建工单"}}),a("a-step",{attrs:{title:"审核中"}}),a("a-step",{attrs:{title:"已审核"}}),a("a-step",{attrs:{title:"处理中"}}),a("a-step",{attrs:{title:"已完成"}}),a("a-step",{attrs:{title:"已复核"}}),a("a-step",{attrs:{title:"已勾住"}})],1),a("a-card",{staticStyle:{"margin-top":"18px"},attrs:{type:"inner",title:"事件状态"}},[t._l(JSON.parse(t.orderDetail.auditor),(function(e){return a("a-descriptions",{key:"auditor"+e.user+e.status,attrs:{size:"small",col:4}},[a("a-descriptions-item",{attrs:{label:"审核人"}},[t._v(" "+t._s(e.user)+" "),1===e.is_superuser?a("span",[t._v("(超级审核人)")]):t._e()]),a("a-descriptions-item",{attrs:{label:"状态"}},[0===e.status?a("a-tag",{attrs:{color:"red"}},[t._v("未审核")]):1===e.status?a("a-tag",{attrs:{color:"green"}},[t._v("已审核")]):a("a-tag",{attrs:{color:"blue"}},[t._v("已驳回")])],1),a("a-descriptions-item",{attrs:{label:"审核时间"}},[t._v(t._s(e.time))]),a("a-descriptions-item",{attrs:{label:"附加信息"}},[t._v(t._s(e.msg))])],1)})),a("a-divider",{staticStyle:{margin:"5px"}}),t._l(JSON.parse(t.orderDetail.reviewer),(function(e){return a("a-descriptions",{key:"reviewer"+e.user+e.status,attrs:{size:"small",col:4}},[a("a-descriptions-item",{attrs:{label:"复核人"}},[t._v(t._s(e.user))]),a("a-descriptions-item",{attrs:{label:"状态"}},[0===e.status?a("a-tag",{attrs:{color:"red"}},[t._v("未复核")]):a("a-tag",{attrs:{color:"green"}},[t._v("已复核")])],1),a("a-descriptions-item",{attrs:{label:"复核时间"}},[t._v(t._s(e.time))]),a("a-descriptions-item",{attrs:{label:"附加信息"}},[t._v(t._s(e.msg))])],1)})),a("a-divider",{staticStyle:{margin:"5px"}}),t._l(JSON.parse(t.orderDetail.executor),(function(e){return a("a-descriptions",{key:"executor"+e.user+e.status,attrs:{size:"small",col:4}},[a("a-descriptions-item",{attrs:{label:"执行人"}},[t._v(t._s(e.user))]),a("a-descriptions-item",{attrs:{label:"状态"}},[t._v("-")]),a("a-descriptions-item",{attrs:{label:"执行时间"}},[t._v(t._s(e.time))]),a("a-descriptions-item",{attrs:{label:"附加信息"}},[t._v(t._s(e.msg))])],1)})),"已关闭"===t.orderDetail.progress?a("div",[a("a-divider",{staticStyle:{margin:"5px"}}),t._l(JSON.parse(t.orderDetail.closer),(function(e){return a("a-descriptions",{key:"closer"+e.user+e.status,attrs:{size:"small",col:4}},[a("a-descriptions-item",{attrs:{label:"关闭人"}},[t._v(t._s(e.user))]),a("a-descriptions-item",{attrs:{label:"状态"}},[t._v("-")]),a("a-descriptions-item",{attrs:{label:"关闭时间"}},[t._v(t._s(e.time))]),a("a-descriptions-item",{attrs:{label:"附加信息"}},[t._v(t._s(e.msg))])],1)}))],2):t._e()],2)],1),a("a-card",{staticStyle:{"margin-top":"-10px"},attrs:{title:"工单内容",bordered:!1}},[a("codemirror",{ref:"myCm",attrs:{options:t.cmOptions},on:{ready:t.onCmReady},model:{value:t.code,callback:function(e){t.code=e},expression:"code"}})],1),a("a-drawer",{attrs:{title:"子任务执行详情",width:"60%",placement:"right",closable:!1,visible:t.visibleDrawer},on:{close:t.onCloseDrawer}},[a("drawerTasksPreview",{attrs:{order_id:this.orderDetail.id}})],1)],1):t._e()],1)},r=[],i=(a("caad"),a("d81d"),a("b0c0"),a("d3b7"),a("5530")),o=a("432b"),n=a("7125"),l=a("4ad3"),c=(a("ffda"),a("0f7c"),a("f4ba"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("a-row",{attrs:{gutter:16}},[a("a-col",{attrs:{span:6}},[a("a-statistic",{staticStyle:{"margin-right":"50px"},attrs:{title:"子任务总数量",value:this.statistics.total},scopedSlots:t._u([{key:"suffix",fn:function(){return[a("a-icon",{attrs:{type:"flag"}})]},proxy:!0}])})],1),a("a-col",{attrs:{span:6}},[a("a-statistic",{staticClass:"demo-class",attrs:{title:"已完成",value:this.statistics.progress_1},scopedSlots:t._u([{key:"suffix",fn:function(){return[a("a-icon",{attrs:{type:"flag"}})]},proxy:!0}])})],1),a("a-col",{attrs:{span:6}},[a("a-statistic",{staticClass:"demo-class",attrs:{title:"未执行",value:this.statistics.progress_0},scopedSlots:t._u([{key:"suffix",fn:function(){return[a("a-icon",{attrs:{type:"flag"}})]},proxy:!0}])})],1),a("a-col",{attrs:{span:6}},[a("a-statistic",{staticClass:"demo-class",attrs:{title:"失败",value:this.statistics.progress_3},scopedSlots:t._u([{key:"suffix",fn:function(){return[a("a-icon",{attrs:{type:"flag"}})]},proxy:!0}])})],1)],1),a("el-divider"),a("div",{staticClass:"table-page-search-wrapper"},[a("a-row",{attrs:{gutter:[8,16]}},[a("a-form",{attrs:{laout:"inline",form:t.form},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleSearch(e)}}},[a("a-col",{attrs:{span:4}},[a("a-form-item",[a("a-select",{directives:[{name:"decorator",rawName:"v-decorator",value:t.decorator["progress"],expression:"decorator['progress']"}],attrs:{placeholder:"状态"}},t._l(t.progress,(function(e){return a("a-select-option",{key:e.key,attrs:{value:e.key}},[t._v(t._s(e.value))])})),1)],1)],1),a("a-col",{attrs:{span:6}},[a("a-form-item",[a("a-input",{directives:[{name:"decorator",rawName:"v-decorator",value:t.decorator["search"],expression:"decorator['search']"}],attrs:{placeholder:"输入要查询的工单内容"}})],1)],1),a("a-col",{attrs:{span:8}},[a("a-form-item",[a("span",{staticClass:"table-page-search-submitButtons"},[a("a-button",{attrs:{type:"primary"},on:{click:t.handleSearch}},[t._v("查询")]),a("a-button",{staticStyle:{"margin-left":"8px"},on:{click:t.resetForm}},[t._v("重置")])],1)])],1)],1)],1)],1),a("a-table",{attrs:{columns:t.table.columns,rowKey:function(t){return t.id},dataSource:t.table.data,pagination:t.pagination,loading:t.loading,size:"middle"},on:{change:t.handleTableChange},scopedSlots:t._u([{key:"num",fn:function(e,s,r){return a("span",{},[a("span",{domProps:{textContent:t._s(r+1)}})])}},{key:"sql",fn:function(e){return a("span",{},[a("a-tooltip",{attrs:{placement:"topLeft"}},[a("template",{slot:"title"},[t._v(t._s(e))]),a("span",{attrs:{href:"#"}},[t._v(t._s(e))])],2)],1)}},{key:"progress",fn:function(e){return a("span",{},["处理中"===e?a("span",{staticStyle:{color:"orange"}},[t._v(t._s(e))]):"已完成"===e?a("span",{staticStyle:{color:"green"}},[t._v(t._s(e))]):"失败"===e?a("span",{staticStyle:{color:"red"}},[t._v(t._s(e))]):"暂停"===e?a("span",{staticStyle:{color:"blue"}},[t._v(t._s(e))]):a("span",[t._v(t._s(e))])])}},{key:"result",fn:function(e,s){return a("span",{},[a("a-icon",{attrs:{type:"eye"},on:{click:function(e){return t.showModal(s)}}})],1)}}])}),a("div",[a("a-modal",{attrs:{title:"任务执行详情",width:"55%"},model:{value:t.modalVisible,callback:function(e){t.modalVisible=e},expression:"modalVisible"}},[a("template",{slot:"footer"},[a("a-button",{key:"back",on:{click:t.handleCancel}},[t._v("Close")])],1),a("div",[a("h5",[t._v("-> 执行日志")]),a("codemirror",{ref:"myCm2",attrs:{options:t.cmOptions},on:{ready:t.onCmReady2},model:{value:t.code2,callback:function(e){t.code2=e},expression:"code2"}})],1),a("div",{staticStyle:{"margin-top":"15px"}},[a("h5",[t._v("-> 回滚SQL")]),a("codemirror",{ref:"myCm1",attrs:{options:t.cmOptions},on:{ready:t.onCmReady1},model:{value:t.code1,callback:function(e){t.code1=e},expression:"code1"}})],1)],2)],1)],1)}),d=[],u=(a("a9e3"),a("ac1f"),a("841c"),{name:"tasks-list",props:{order_id:Number},data:function(){return{modalLoading:!1,modalVisible:!1,timer:"",loading:!1,progress:n["e"],statistics:{total:0,progress_0:0,progress_1:0,progress_3:0},table:{columns:null,data:null},pagination:{current:1,pageSize:10,total:0,pageSizeOptions:["10","20"],showSizeChanger:!0},decorator:{progress:["progress",{rules:[{required:!1}]}],search:["search",{rules:[{required:!1}]}]},code1:"",code2:"",cmOptions:{mode:"text/x-mysql",indentUnit:2,tabSize:2,indentWithTabs:!0,smartIndent:!0,autoRefresh:!0,lineWrapping:!0,viewportMargin:1/0,readOnly:!0,autofocus:!1},form:this.$form.createForm(this)}},methods:{handleTableChange:function(t){this.pagination.current=t.current,this.pagination.pageSize=t.pageSize,this.fetchData()},fetchData:function(){var t=this;Object(l["o"])({order_id:this.order_id}).then((function(e){t.task_id=e.data;var a=Object(i["a"])({page_size:t.pagination.pageSize,page:t.pagination.current,task_id:t.task_id},t.filters);t.loading=!0,Object(l["q"])(a).then((function(e){t.pagination.total=e.count,t.loading=!1,t.table.columns=e.results.columns,t.table.data=e.results.data.data,t.statistics.total=e.results.data.total,t.statistics.progress_0=e.results.data.progress_0,t.statistics.progress_1=e.results.data.progress_1,t.statistics.progress_3=e.results.data.progress_3})).catch((function(e){t.$message.error(e.response.data.detail,5),setTimeout((function(){t.$router.push({name:"view.sqlorders.list"})}),5e3)})).finally((function(){t.loading=!1}))}))},handleSearch:function(t){var e=this;t.preventDefault(),this.form.validateFields((function(t,a){t||(e.filters={progress:a["progress"],search:a["search"]},e.pagination.current=1,e.fetchData())}))},resetForm:function(){this.form.resetFields()},getTResult:function(t){var e=this;Object(l["r"])(t.id).then((function(t){e.codemirror1.setValue(t.data.rollback_sql),e.codemirror2.setValue(t.data.execute_log),setTimeout((function(){e.resultLoading=!1}),500)})).catch((function(t){setTimeout((function(){e.resultLoading=!1}),500)}))},showModal:function(t){this.modalVisible=!0,this.getTResult(t)},handleCancel:function(t){this.modalVisible=!1},onCmReady1:function(t){t.setSize("height","250px")},onCmReady2:function(t){t.setSize("height","250px")}},computed:{codemirror1:function(){return this.$refs.myCm1.codemirror},codemirror2:function(){return this.$refs.myCm2.codemirror}},destroyed:function(){clearInterval(this.timer)},mounted:function(){var t=this;this.fetchData(),this.timer&&clearInterval(this.timer),this.timer=setInterval((function(){setTimeout(t.fetchData(),0)}),1e4)}}),m=u,p=(a("996a"),a("2877")),h=Object(p["a"])(m,c,d,!1,null,null,null),f=h.exports,b={okText:"确认",cancelText:"取消",action:""},v={okText:"提交",cancelText:"关闭",action:"close"},g={btnDisabled:!1,closeDisabled:!1},_={name:"detail",mixins:[o["a"]],components:{drawerTasksPreview:f},data:function(){return{visible:!1,visibleDrawer:!1,closeVisible:!1,loading:!1,executeLoading:!1,envs:[],hookLoading:!1,hookVisible:!1,btnStatus:g,confirmMsg:"",orderDetail:"",toUrl:"",confirmBtnTips:b,code:"",cmOptions:{mode:"text/x-mysql",indentUnit:2,tabSize:2,indentWithTabs:!0,smartIndent:!0,autoRefresh:!0,lineNumbers:!0,readOnly:!0,focuse:!1},schemas:[],sql_envs:[],resetAuditStatus:"ON",remarks:n["a"],ruleForm:{title:"",current_database:"",env_id:"",database:"",remark:""}}},methods:{getEnvs:function(){var t=this;l["j"].then((function(e){t.envs=e.data}))},showTasksDrawer:function(){this.visibleDrawer=!0},onCloseDrawer:function(){this.visibleDrawer=!1},getOrderDetail:function(){var t=this;Object(l["m"])(this.$route.params.order_id).then((function(e){t.orderDetail=e.data}))},changeEnvs:function(t){var e=this;this.ruleForm.database="";var a={env_id:t,use_type:0,rds_category:this.orderDetail.rds_category};Object(l["k"])(a).then((function(t){e.schemas=t.data}))},onCmReady:function(t){t.setSize("height","600px"),t.setValue(this.orderDetail.contents)},refresh:function(){var t=this;this.loading=!0,this.getOrderDetail(),setTimeout((function(){t.loading=!1}),1e3)},handleCommit:function(t,e){var a=this;if(this.confirmMsg.length>128)return this.$message.error("提交失败，消息长度不能超过128个字符"),this.hideModal(),!1;var s={action:e,msg:this.confirmMsg,btn:t,pk:this.orderDetail.id};Object(l["v"])(s).then((function(t){"0000"===t.code?a.$message.success(t.message):a.$message.error(JSON.stringify(t.message))})).catch((function(t){a.$message.error(t)})).finally((function(){a.hideModal(),a.refresh()}))},generateSqlOrdersTasks:function(){var t=this;this.executeLoading=!0;var e={id:this.orderDetail.id};Object(l["i"])(e).then((function(e){"0000"===e.code?t.$router.push("/sqlorders/tasks/".concat(e.data)):t.$message.error(e.message)})).catch((function(e){t.$message.error(e)})).finally((function(){t.executeLoading=!1}))},showModal:function(){this.visible=!0},hideModal:function(){this.visible=!1},handleOk:function(t){this.handleCommit("ok",b.action),this.hideModal()},handleCancel:function(){this.handleCommit("cancel",b.action),this.hideModal()},showHookModal:function(){var t=this;this.ruleForm.title=this.orderDetail.title,this.ruleForm.current_database=this.orderDetail.database,this.sql_envs=[],this.envs.map((function(e){e.name!=t.orderDetail.env_id&&t.sql_envs.push(e)})),this.hookVisible=!0},hideHookModal:function(){this.hookVisible=!1},handleHookOk:function(){var t=this,e=Object(i["a"])({id:this.orderDetail.id,reset:this.resetAuditStatus},this.ruleForm);Object(l["a"])(e).then((function(e){"0000"===e.code?t.$router.push("/sqlorders/list"):t.$message.error(e.message)}))},handleHookCancel:function(){this.hideHookModal()},showCloseModal:function(){this.closeVisible=!0},hideCloseModal:function(){this.closeVisible=!1},handleCloseOk:function(t){this.handleCommit("ok",v.action),this.hideCloseModal()},handleCloseCancel:function(){this.hideCloseModal()},onRestChange:function(t){this.resetAuditStatus=t?"ON":"OFF"}},mounted:function(){this.getEnvs(),this.getOrderDetail()},filters:{btnTitle:function(t){return"待审核"===t?(g.btnDisabled=!1,g.closeDisabled=!1,b.okText="同意",b.cancelText="驳回",b.action="approve","审核"):["已批准","处理中"].includes(t)?(g.btnDisabled=!1,g.closeDisabled=!1,b.okText="处理中",b.cancelText="执行完成",b.action="feedback","反馈"):"已完成"===t?(g.btnDisabled=!1,g.closeDisabled=!0,b.okText="已复核",b.cancelText="关闭窗口",b.action="review","复核"):["已关闭","已勾住","已驳回","已复核"].includes(t)?(g.btnDisabled=!0,g.closeDisabled=!0,"完成"):void 0}},computed:{codemirror:function(){return this.$refs.myCm.codemirror},currentStatus:function(){return"已驳回"===this.orderDetail.progress?2:"已关闭"===this.orderDetail.progress?4:"待审核"===this.orderDetail.progress?1:"已批准"===this.orderDetail.progress?2:"处理中"===this.orderDetail.progress?3:"已完成"===this.orderDetail.progress?4:"已复核"===this.orderDetail.progress?5:6}}},k=_,y=(a("dcd7"),Object(p["a"])(k,s,r,!1,null,"513cac92",null));e["default"]=y.exports},"646d":function(t,e,a){},"996a":function(t,e,a){"use strict";var s=a("9a68"),r=a.n(s);r.a},"9a68":function(t,e,a){},dcd7:function(t,e,a){"use strict";var s=a("646d"),r=a.n(s);r.a}}]);