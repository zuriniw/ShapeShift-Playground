from cmu_graphics import *
from Components import TypicleComponent

class CircleCreator(TypicleComponent):
    def __init__(self, app):
        inputs = ['point', 'radius']
        outputs = ['circle']
        name = 'Draw\nCirc\nO'
        self.isGeo = True
        self.isDisplay = True
        super().__init__(app, inputs, outputs, name)
        
        # 设置默认值
        self.inputDefaultValue = {
            'point': ['point',(app.x0, app.y0)],
            'radius': 40
        }
        
        # 为输入节点设置默认值
        for node in self.inputNodes:
            node.value = self.inputDefaultValue[node.name]
            
        # 初始化输出节点值
        self.outputNodes[0].value = ['cir', (app.x0, app.y0), 40]
        self.hasAllInputs = True
    
    def calculate(self):
        point_val = self.inputNodes[0].value[1]
        radius_val = abs(self.inputNodes[1].value) if self.inputNodes[1].value is not None else None
        return [['cir', point_val, radius_val]]
    
    def draw(self):
        if self.hasAllInputs:
            x, y = self.inputNodes[0].value[1]
            radius = abs(self.inputNodes[1].value)
            if int(radius) != 0:
                drawCircle(x, y, radius, fill=None, border='blue', visible=self.isDisplay)

class RectCreator(TypicleComponent):
    def __init__(self, app):
        inputs = ['point', 'width', 'height']
        outputs = ['rect']
        name = 'Draw\nRect\n⬚'
        self.isGeo = True
        self.isDisplay = True
        super().__init__(app, inputs, outputs, name)
        
        # 设置默认值
        self.inputDefaultValue = {
            'point': ['point',(app.x0, app.y0)],
            'width': 40,
            'height': 40
        }
        
        # 为输入节点设置默认值
        for node in self.inputNodes:
            node.value = self.inputDefaultValue[node.name]
            
        # 初始化输出节点值，与 CircleCreator 保持一致
        self.outputNodes[0].value = ['rect', (app.x0, app.y0), 40, 40]
        self.hasAllInputs = True
    
    def calculate(self):
        point_val = self.inputNodes[0].value[1]
        width_val = abs(self.inputNodes[1].value)
        height_val = abs(self.inputNodes[2].value)
        return [['rect', point_val, width_val, height_val]]

    
    def draw(self):
        if self.hasAllInputs:
            x, y = self.inputNodes[0].value[1]
            width = abs(self.inputNodes[1].value)
            height = abs(self.inputNodes[2].value)
            if int(width) != 0 and int(height) != 0:
                drawRect(x - width/2, y - height/2, width, height,
                        fill=None, border='blue')
