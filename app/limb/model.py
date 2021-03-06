from app import db


class Limb(db.Model):
    cols = ['id', 'name', 'ip', 'area', 'sub_area', 'ssh_key']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    ip = db.Column(db.String(120))
    area = db.Column(db.String(120))
    sub_area = db.Column(db.String(120))
    ssh_key = db.Column(db.String)

    def __repr__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "ip": self.ip,
            "area": self.area,
            "sub_area": self.sub_area,
            "ssh_key": self.ssh_key
        })
