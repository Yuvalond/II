#include "cl_application.h"
#include "cl_1.h"
#include "cl_2.h"
#include "cl_3.h"
#include "cl_4.h"
#include "cl_5.h"
#include "cl_6.h"
cl_application::cl_application(cl_base* p_head_object) : cl_base(p_head_object) {

};

void cl_application::build_tree_objects(){
	string s_head, s_sub;
	cl_base* p_head = this, p_sub = nullptr;
	
	int i_class, i_state;
	
	cin >> s_head;
	
	this->set_name(s_head);

	while (true) {
		cin >> s_head;
		if (s_head == "endtree")
			break;
		cin >> s_sub >> i_class;
		p_head = find_object_from_root(s_head);
		switch(i_class){
			case 1:
				p_head = new cl_1(p_head,s_sub);
				break;
			case 2:
				p_head = new cl_2(p_head,s_sub);
				break;
			case 3:
				p_head = new cl_3(p_head,s_sub);
				break;
			case 4:
				p_head = new cl_4(p_head,s_sub);
				break;
			case 5:
				p_head = new cl_5(p_head,s_sub);
				break;
			case 6:
				p_head = new cl_6(p_head,s_sub);
				break;
			}
	}
	while (cin >> s_head)
	{
		cin >> i_state;
		p_head = this->find_object_from_root(s_head);
		if(p_head->can_be_ready()){
			p_head->set_ready(i_state);
		}
	}
	
}

	


void cl_application::set_object_ready(cl_base* p_object, int state_number) {
	if (!p_object) {
		return;
	}
	p_object->set_state(state_number);
}

int cl_application::exec_app() {
	int level = 0;
	cout << "Object tree" << endl;
	print_tree(level);
	cout << "The tree of objects and their readiness" << endl;
	print_status(level);
	return 0;
}